"""Catalog table sanity — every code maps cleanly and labels follow the game UI."""

from __future__ import annotations

from fbpro98_profile import ProfileType
from pnfl_profile.rules import (
    PASS_LONG_LEFT,
    PASS_LONG_MIDDLE,
    PASS_LONG_RIGHT,
    PASS_MEDIUM_LEFT,
    PASS_MEDIUM_MIDDLE,
    PASS_MEDIUM_RIGHT,
    PASS_SHORT_LEFT,
    PASS_SHORT_MIDDLE,
    PASS_SHORT_RIGHT,
    RAZZLE_DAZZLE_PASS,
    RUN_LEFT,
)

from pnfl_profiler.catalog import (
    DEFENSE_CATEGORIES,
    OFFENSE_CATEGORIES,
    categories_for,
    category_for_code,
)


def test_offense_catalog_has_13_entries() -> None:
    assert len(OFFENSE_CATEGORIES) == 13


def test_defense_catalog_has_10_entries() -> None:
    assert len(DEFENSE_CATEGORIES) == 10


def test_offense_options_are_singletons() -> None:
    for opt in OFFENSE_CATEGORIES:
        assert len(opt.codes) == 1
        assert opt.default_code in opt.codes


def test_defense_collapses_directional_pass() -> None:
    labels = {opt.label: opt for opt in DEFENSE_CATEGORIES}
    assert labels["PASS LONG"].codes == frozenset(
        {PASS_LONG_LEFT, PASS_LONG_MIDDLE, PASS_LONG_RIGHT}
    )
    assert labels["PASS MEDIUM"].codes == frozenset(
        {PASS_MEDIUM_LEFT, PASS_MEDIUM_MIDDLE, PASS_MEDIUM_RIGHT}
    )
    assert labels["PASS SHORT"].codes == frozenset(
        {PASS_SHORT_LEFT, PASS_SHORT_MIDDLE, PASS_SHORT_RIGHT}
    )
    assert labels["PASS LONG"].default_code == PASS_LONG_MIDDLE
    assert labels["PASS MEDIUM"].default_code == PASS_MEDIUM_MIDDLE
    assert labels["PASS SHORT"].default_code == PASS_SHORT_MIDDLE


def test_categories_for_dispatch() -> None:
    assert categories_for(ProfileType.OFFENSE) is OFFENSE_CATEGORIES
    assert categories_for(ProfileType.DEFENSE) is DEFENSE_CATEGORIES


def test_category_for_code_finds_options() -> None:
    opt = category_for_code(RUN_LEFT, ProfileType.OFFENSE)
    assert opt is not None and opt.label == "RUN LEFT"
    opt_def = category_for_code(PASS_LONG_RIGHT, ProfileType.DEFENSE)
    assert opt_def is not None and opt_def.label == "PASS LONG"


def test_category_for_code_returns_none_for_disallowed() -> None:
    # PUNT (0x13) is not PNFL-allowed in either offense or defense dropdowns.
    assert category_for_code(0x13, ProfileType.OFFENSE) is None
    assert category_for_code(0x13, ProfileType.DEFENSE) is None


def test_razzle_dazzle_pass_in_both_sides() -> None:
    assert category_for_code(RAZZLE_DAZZLE_PASS, ProfileType.OFFENSE) is not None
    assert category_for_code(RAZZLE_DAZZLE_PASS, ProfileType.DEFENSE) is not None


def test_all_offense_labels_uppercase() -> None:
    for opt in OFFENSE_CATEGORIES:
        assert opt.label == opt.label.upper()


def test_all_defense_labels_uppercase() -> None:
    for opt in DEFENSE_CATEGORIES:
        assert opt.label == opt.label.upper()
