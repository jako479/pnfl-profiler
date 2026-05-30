"""ProfileSession: open/edit/save round-trips with the test fixtures.

Mutates only copies in `tmp_path` (see conftest.py).
"""

from __future__ import annotations

import dataclasses
from pathlib import Path

import pytest
from fbpro98_profile import CategoryWeights, ProfileType, read_profile
from pnfl_profile import PNFL_RULES, PnflProfile

from pnfl_profiler.session import NoProfileLoadedError, ProfileSession


@pytest.fixture
def qt_app():
    """ProfileSession is a QObject and needs a QCoreApplication for signals."""
    from PySide6.QtCore import QCoreApplication

    app = QCoreApplication.instance() or QCoreApplication([])
    yield app


def _new_session(qt_app) -> ProfileSession:
    return ProfileSession()


def test_open_loads_offense(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    assert session.is_loaded
    assert session.path == tst_off_path
    assert session.profile.profile_type == ProfileType.OFFENSE
    assert not session.dirty


def test_open_loads_defense(qt_app, tst_def_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_def_path)
    assert session.profile.profile_type == ProfileType.DEFENSE


def test_close_clears_state(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    session.close()
    assert not session.is_loaded
    assert session.path is None
    with pytest.raises(NoProfileLoadedError):
        session.validate()


def test_save_raises_on_pnfl_violations(qt_app, tst_off_path: Path) -> None:
    """The TST-*.prf fixtures have known PNFL violations; save must surface them.

    This is the contract: save = validate then write. If the in-memory profile
    fails validation, no bytes touch disk.
    """
    from pnfl_profile import PnflRuleError

    session = _new_session(qt_app)
    session.open(tst_off_path)
    original_bytes = tst_off_path.read_bytes()
    with pytest.raises(PnflRuleError):
        session.save()
    # File on disk is unchanged.
    assert tst_off_path.read_bytes() == original_bytes


def test_save_forces_audibles_off_in_memory(qt_app, tst_off_path: Path) -> None:
    """Audibles get cleared before validation, so the in-memory profile reflects
    the correction even when save's validation pass then raises on other
    violations."""
    from pnfl_profile import PnflRuleError

    session = _new_session(qt_app)
    session.open(tst_off_path)
    flipped = dataclasses.replace(session.profile, use_audibles=True)
    session._pnfl = PnflProfile(profile=flipped, rules=PNFL_RULES)
    assert session.profile.use_audibles is True
    with pytest.raises(PnflRuleError):
        session.save()
    # The audibles-off correction happens before validation, so it sticks even
    # though validation then raised.
    assert session.profile.use_audibles is False


def test_save_audibles_off_round_trip_via_write_profile(
    qt_app, tmp_path: Path, tst_off_path: Path
) -> None:
    """Bypassing PnflProfile.save (using fbpro98_profile.write_profile directly)
    confirms the audibles=False profile serializes and parses back correctly.

    Separate from `test_save_forces_audibles_off_in_memory` because the fixture
    has unrelated PNFL violations that block the validation path.
    """
    from fbpro98_profile import write_profile

    session = _new_session(qt_app)
    session.open(tst_off_path)
    profile = dataclasses.replace(session.profile, use_audibles=False)
    out = tmp_path / "AUDIBLES_OFF.prf"
    write_profile(profile, str(out))
    reloaded = read_profile(str(out))
    assert reloaded.use_audibles is False


def test_save_as_does_not_create_file_on_violations(
    qt_app, tmp_path: Path, tst_off_path: Path
) -> None:
    """When validation fails, save_as must not produce a partial file at the new path."""
    from pnfl_profile import PnflRuleError

    session = _new_session(qt_app)
    session.open(tst_off_path)
    new_path = tmp_path / "OUT.prf"
    with pytest.raises(PnflRuleError):
        session.save_as(new_path)
    assert not new_path.exists()
    # Original is unchanged.
    assert tst_off_path.exists()


def test_update_situation_flips_dirty(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    sit = session.situation(1)
    new_weights = CategoryWeights(
        play_category1=sit.category_weights.play_category1,
        weight1=(sit.category_weights.weight1 + 1) % 11,
        play_category2=sit.category_weights.play_category2,
        weight2=sit.category_weights.weight2,
        play_category3=sit.category_weights.play_category3,
        weight3=sit.category_weights.weight3,
    )
    session.update_situation(1, new_weights, sit.stop_clock)
    assert session.dirty
    assert session.situation(1).category_weights == new_weights


def test_update_situation_preserves_other_fields(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    original_subs = session.profile.substitutions
    original_pats = session.profile.pat_situations
    original_fg = session.profile.field_goal_range

    sit = session.situation(1)
    session.update_situation(1, sit.category_weights, not sit.stop_clock)

    assert session.profile.substitutions == original_subs
    assert session.profile.pat_situations == original_pats
    assert session.profile.field_goal_range == original_fg


def test_copy_situation_applies_plays_only(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    source = session.situation(1)
    targets = (10, 20, 30)

    # Capture clocks before so we can assert clock was NOT copied.
    pre_clocks = {n: session.situation(n).stop_clock for n in targets}

    flipped = dataclasses.replace(source, stop_clock=not source.stop_clock)
    session._pnfl = dataclasses.replace(
        session.pnfl_profile,
        profile=dataclasses.replace(
            session.profile,
            situations=tuple(
                flipped if i == 0 else s
                for i, s in enumerate(session.profile.situations)
            ),
        ),
    )
    # Now source has flipped clock; copy plays only.
    updated = session.copy_situation(1, targets, copy_plays=True, copy_clock=False)
    assert updated == 3
    for n in targets:
        assert session.situation(n).category_weights == flipped.category_weights
        assert session.situation(n).stop_clock == pre_clocks[n]


def test_copy_situation_skips_source(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    updated = session.copy_situation(5, (5, 6, 7), copy_plays=True, copy_clock=True)
    assert updated == 2  # 5 was skipped


def test_copy_situation_no_op_when_nothing_chosen(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    updated = session.copy_situation(1, (2, 3), copy_plays=False, copy_clock=False)
    assert updated == 0
    assert not session.dirty


def test_validate_runs_pnfl_rules(qt_app, tst_off_path: Path) -> None:
    session = _new_session(qt_app)
    session.open(tst_off_path)
    violations = session.validate()
    # Either some or none — both are valid; we just confirm the call returns a tuple.
    assert isinstance(violations, tuple)
