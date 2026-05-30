"""Main window — menu bar + horizontally-scrolling field-position pane row.

Layout, menu structure, shortcuts, and action labels live in
`forms/main_window.ui` (editable in Qt Designer). This class adds three
`FieldPositionPane` instances into the .ui's `paneRowLayout` and connects every
`QAction` to the appropriate session / dialog slot.
"""

from __future__ import annotations

from pathlib import Path

from fbpro98_profile import FieldPosition
from pnfl_profile import PnflRuleError
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from pnfl_profiler.session import ProfileSession
from pnfl_profiler.ui.check_profile_dialog import CheckProfileDialog
from pnfl_profiler.ui.copy_dialog import CopyDialog
from pnfl_profiler.ui.field_position_pane import FieldPositionPane
from pnfl_profiler.ui.forms.main_window_ui import Ui_MainWindow
from pnfl_profiler.ui.situation_panel import SituationEditPanel

# v1 ships three of the five field-position buckets visible at once; the rest
# scroll into view. The middle bands are the most-edited per the plan.
_INITIAL_PANES = (
    FieldPosition.DEF_5_TO_DEF_35,
    FieldPosition.DEF_35_TO_OFF_35,
    FieldPosition.OFF_35_TO_OFF_5,
)


class MainWindow(QMainWindow):
    def __init__(self, session: ProfileSession | None = None) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._session = session if session is not None else ProfileSession()
        self._panes: dict[FieldPosition, FieldPositionPane] = {}

        for fp in _INITIAL_PANES:
            pane = FieldPositionPane(fp)
            pane.add_panel_requested.connect(self._on_add_panel_requested)
            self._panes[fp] = pane
            self.ui.paneRowLayout.addWidget(pane)
        self.ui.paneRowLayout.addStretch()

        self.ui.actionOpen.triggered.connect(self._on_open)
        self.ui.actionSave.triggered.connect(self._on_save)
        self.ui.actionSaveAs.triggered.connect(self._on_save_as)
        self.ui.actionClose.triggered.connect(self._on_close)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionCheckProfile.triggered.connect(self._on_check)

        self._session.profile_loaded.connect(self._on_profile_loaded)
        self._session.profile_closed.connect(self._on_profile_closed)
        self._session.dirty_changed.connect(self._refresh_title)
        self._refresh_title()

    @property
    def session(self) -> ProfileSession:
        return self._session

    # ---------------------------------------------------------------
    # Menu actions
    # ---------------------------------------------------------------

    def _on_open(self) -> None:
        if not self._confirm_discard_changes("Open a different profile?"):
            return
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open profile",
            "",
            "Profile files (*.prf);;All files (*)",
        )
        if not path:
            return
        try:
            self._session.open(path)
        except Exception as exc:
            QMessageBox.critical(
                self, "Open failed", f"Could not open {path}:\n\n{exc}"
            )

    def _on_save(self) -> None:
        if not self._session.is_loaded:
            return
        if self._session.path is None:
            self._on_save_as()
            return
        self._try_save(self._session.path, save_as=False)

    def _on_save_as(self) -> None:
        if not self._session.is_loaded:
            return
        suggested = str(self._session.path) if self._session.path else ""
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save profile as",
            suggested,
            "Profile files (*.prf);;All files (*)",
        )
        if not path:
            return
        self._try_save(Path(path), save_as=True)

    def _on_close(self) -> None:
        if not self._session.is_loaded:
            return
        if not self._confirm_discard_changes("Close this profile?"):
            return
        self._session.close()

    def _on_check(self) -> None:
        if not self._session.is_loaded:
            return
        violations = self._session.validate()
        dialog = CheckProfileDialog(violations, self)
        dialog.jump_to_situation.connect(self._on_jump_to_situation)
        dialog.exec()

    # ---------------------------------------------------------------
    # Session signal handlers
    # ---------------------------------------------------------------

    def _on_profile_loaded(self) -> None:
        profile_type = self._session.profile.profile_type
        for pane in self._panes.values():
            pane.clear()
            pane.set_profile_type(profile_type)
        self._refresh_title()

    def _on_profile_closed(self) -> None:
        for pane in self._panes.values():
            pane.clear()
        self._refresh_title()

    # ---------------------------------------------------------------
    # Pane / panel signal handlers
    # ---------------------------------------------------------------

    def _on_add_panel_requested(self, field_position: FieldPosition) -> None:
        if not self._session.is_loaded:
            return
        pane = self._panes[field_position]
        n = pane.default_situation_number()
        panel = pane.add_panel(self._session.situation(n))
        self._wire_panel(panel)

    def _wire_panel(self, panel: SituationEditPanel) -> None:
        panel.situation_changed.connect(self._on_situation_changed)
        panel.copy_requested.connect(self._on_copy_requested)

    def _on_situation_changed(self, n: int, weights, stop_clock: bool) -> None:
        try:
            self._session.update_situation(n, weights, stop_clock)
        except Exception as exc:
            QMessageBox.warning(self, "Invalid edit", str(exc))

    def _on_copy_requested(self, source_situation_number: int) -> None:
        dialog = CopyDialog(source_situation_number, self)
        if dialog.exec() != int(CopyDialog.DialogCode.Accepted):
            return
        targets = dialog.destination_situation_numbers()
        updated = self._session.copy_situation(
            source_situation_number,
            targets,
            copy_plays=dialog.copy_plays(),
            copy_clock=dialog.copy_clock(),
        )
        QMessageBox.information(
            self, "Copy complete", f"Applied to {updated} situation(s)."
        )

    def _on_jump_to_situation(self, situation_number: int) -> None:
        situation = self._session.situation(situation_number)
        field = situation.field_position
        pane = self._panes.get(field)
        if pane is None:
            QMessageBox.information(
                self,
                "Field position off-screen",
                f"Situation {situation_number} is in field position "
                f"'{field.name}', which has no pane in v1.",
            )
            return
        panel = pane.find_panel_for_situation(situation_number)
        if panel is None:
            panel = pane.add_panel(situation)
            self._wire_panel(panel)
        panel.setFocus()

    # ---------------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------------

    def _try_save(self, path: Path, *, save_as: bool) -> None:
        try:
            if save_as:
                self._session.save_as(path)
            else:
                self._session.save()
        except PnflRuleError as err:
            self._show_violations(err.violations)
        except Exception as exc:
            QMessageBox.critical(self, "Save failed", f"Could not save:\n\n{exc}")
        else:
            self._refresh_title()

    def _show_violations(self, violations: tuple) -> None:
        lines = [f"{v.rule_name}: {v.message}" for v in violations[:10]]
        if len(violations) > 10:
            lines.append(f"... and {len(violations) - 10} more.")
        QMessageBox.critical(
            self,
            "Save blocked by PNFL rule violations",
            "\n".join(lines) or "Validation failed.",
        )

    def _confirm_discard_changes(self, prompt: str) -> bool:
        if not self._session.is_loaded or not self._session.dirty:
            return True
        yes_no = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        answer = QMessageBox.question(
            self,
            "Unsaved changes",
            f"Discard unsaved changes? {prompt}",
            yes_no,
        )
        return answer == QMessageBox.StandardButton.Yes

    def _refresh_title(self, *_args) -> None:
        base = "pnfl-profiler"
        if not self._session.is_loaded:
            self.setWindowTitle(base)
            return
        name = self._session.path.name if self._session.path else "(unsaved)"
        marker = "*" if self._session.dirty else ""
        self.setWindowTitle(f"{base} — {name}{marker}")

    # ---------------------------------------------------------------
    # Close intercept
    # ---------------------------------------------------------------

    def closeEvent(self, event: QCloseEvent) -> None:
        if self._confirm_discard_changes("Exit?"):
            event.accept()
        else:
            event.ignore()
