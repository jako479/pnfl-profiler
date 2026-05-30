"""Editable in-memory session over a single `PnflProfile`.

`ProfileSession` owns the loaded profile, the dirty bit, and the path on disk
(if any). It mediates every edit so the UI layer never touches frozen
dataclasses directly. PySide6 Signals notify the UI of state changes.
"""

from __future__ import annotations

import dataclasses
from collections.abc import Iterable
from pathlib import Path

from fbpro98_profile import (
    CategoryWeights,
    Profile,
    Situation,
)
from pnfl_profile import (
    PNFL_RULES,
    PnflProfile,
    PnflRules,
    Violation,
)
from PySide6.QtCore import QObject, Signal


class NoProfileLoadedError(RuntimeError):
    """Raised when a session operation is called with no profile loaded."""


class ProfileSession(QObject):
    """Owns the in-memory `PnflProfile` and dispatches edits.

    Emits:
        profile_loaded(): a new profile has been loaded; UI should rebuild.
        profile_modified(): the profile in memory has changed.
        profile_closed(): the profile has been closed; UI should clear.
        dirty_changed(bool): the dirty flag has flipped.
    """

    profile_loaded = Signal()
    profile_modified = Signal()
    profile_closed = Signal()
    dirty_changed = Signal(bool)

    def __init__(
        self, rules: PnflRules = PNFL_RULES, parent: QObject | None = None
    ) -> None:
        super().__init__(parent)
        self._rules = rules
        self._pnfl: PnflProfile | None = None
        self._path: Path | None = None
        self._dirty: bool = False

    # ---------------------------------------------------------------
    # Read-only access
    # ---------------------------------------------------------------

    @property
    def is_loaded(self) -> bool:
        return self._pnfl is not None

    @property
    def path(self) -> Path | None:
        return self._path

    @property
    def dirty(self) -> bool:
        return self._dirty

    @property
    def pnfl_profile(self) -> PnflProfile:
        if self._pnfl is None:
            raise NoProfileLoadedError("No profile loaded")
        return self._pnfl

    @property
    def profile(self) -> Profile:
        return self.pnfl_profile.profile

    def situation(self, situation_number: int) -> Situation:
        return self.profile.situations[situation_number - 1]

    # ---------------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------------

    def open(self, path: Path | str) -> None:
        """Load a `.prf` from disk and replace the current session state."""
        path_obj = Path(path)
        self._pnfl = PnflProfile.from_file(str(path_obj), self._rules)
        self._path = path_obj
        self._set_dirty(False)
        self.profile_loaded.emit()

    def close(self) -> None:
        """Drop the loaded profile without saving."""
        self._pnfl = None
        self._path = None
        self._set_dirty(False)
        self.profile_closed.emit()

    def save(self) -> None:
        """Save to the loaded path. Forces audibles off; raises `PnflRuleError`
        on validation failure (file untouched in that case)."""
        if self._path is None:
            raise NoProfileLoadedError("No path; use save_as")
        self._save_to(self._path)

    def save_as(self, path: Path | str) -> None:
        """Save to a new path and track it as the session's path going forward."""
        path_obj = Path(path)
        self._save_to(path_obj)
        self._path = path_obj

    def validate(self) -> tuple[Violation, ...]:
        return self.pnfl_profile.validate()

    # ---------------------------------------------------------------
    # Edit operations
    # ---------------------------------------------------------------

    def update_situation(
        self,
        situation_number: int,
        weights: CategoryWeights,
        stop_clock: bool,
    ) -> None:
        """Replace one situation's category weights and clock flag."""
        new_situation = dataclasses.replace(
            self.situation(situation_number),
            category_weights=weights,
            stop_clock=stop_clock,
        )
        self._replace_situations({situation_number: new_situation})

    def copy_situation(
        self,
        source_number: int,
        target_numbers: Iterable[int],
        copy_plays: bool,
        copy_clock: bool,
    ) -> int:
        """Copy plays and/or stop-clock from the source to each target.

        Returns the number of targets actually updated (excludes the source
        itself if present in `target_numbers`).
        """
        if not copy_plays and not copy_clock:
            return 0
        source = self.situation(source_number)
        replacements: dict[int, Situation] = {}
        for n in target_numbers:
            if n == source_number:
                continue
            existing = self.situation(n)
            new_weights = (
                source.category_weights if copy_plays else existing.category_weights
            )
            new_clock = source.stop_clock if copy_clock else existing.stop_clock
            replacements[n] = dataclasses.replace(
                existing,
                category_weights=new_weights,
                stop_clock=new_clock,
            )
        if not replacements:
            return 0
        self._replace_situations(replacements)
        return len(replacements)

    # ---------------------------------------------------------------
    # Internals
    # ---------------------------------------------------------------

    def _replace_situations(self, replacements: dict[int, Situation]) -> None:
        current = list(self.profile.situations)
        for n, s in replacements.items():
            current[n - 1] = s
        new_profile = dataclasses.replace(self.profile, situations=tuple(current))
        self._pnfl = PnflProfile(profile=new_profile, rules=self._rules)
        self._set_dirty(True)
        self.profile_modified.emit()

    def _save_to(self, path: Path) -> None:
        pnfl = self.pnfl_profile
        if pnfl.profile.use_audibles:
            profile_off = dataclasses.replace(pnfl.profile, use_audibles=False)
            pnfl = PnflProfile(profile=profile_off, rules=self._rules)
            self._pnfl = pnfl
        pnfl.save(str(path))
        self._set_dirty(False)

    def _set_dirty(self, value: bool) -> None:
        if self._dirty == value:
            return
        self._dirty = value
        self.dirty_changed.emit(value)
