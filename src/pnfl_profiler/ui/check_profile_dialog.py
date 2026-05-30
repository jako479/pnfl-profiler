"""Check Profile dialog — walks PNFL rule violations one at a time.

Layout lives in `forms/check_profile_dialog.ui` (editable in Qt Designer).
"""

from __future__ import annotations

from pnfl_profile import Violation
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QWidget

from pnfl_profiler.ui.forms.check_profile_dialog_ui import Ui_CheckProfileDialog


class CheckProfileDialog(QDialog):
    jump_to_situation = Signal(int)

    def __init__(
        self, violations: tuple[Violation, ...], parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self._violations = violations
        self._index = 0

        self.ui = Ui_CheckProfileDialog()
        self.ui.setupUi(self)

        self.ui.prevButton.clicked.connect(self._on_prev)
        self.ui.nextButton.clicked.connect(self._on_next)
        self.ui.jumpButton.clicked.connect(self._on_jump)

        self._refresh()

    # Expose key widgets under the names the smoke tests rely on.
    @property
    def _header(self):
        return self.ui.headerLabel

    @property
    def _body(self):
        return self.ui.bodyText

    def _refresh(self) -> None:
        n = len(self._violations)
        if n == 0:
            self.ui.headerLabel.setText("<b>No violations</b>")
            self.ui.bodyText.setPlainText("This profile passes every PNFL rule.")
            self.ui.prevButton.setEnabled(False)
            self.ui.nextButton.setEnabled(False)
            self.ui.jumpButton.setEnabled(False)
            return
        v = self._violations[self._index]
        self.ui.headerLabel.setText(
            f"<b>Violation {self._index + 1} of {n}</b> — {v.rule_name}"
        )
        situation_line = (
            f"Situation #{v.situation_number}\n\n"
            if v.situation_number is not None
            else ""
        )
        self.ui.bodyText.setPlainText(f"{situation_line}{v.message}")
        self.ui.prevButton.setEnabled(self._index > 0)
        self.ui.nextButton.setEnabled(self._index < n - 1)
        self.ui.jumpButton.setEnabled(v.situation_number is not None)

    def _on_prev(self) -> None:
        if self._index > 0:
            self._index -= 1
            self._refresh()

    def _on_next(self) -> None:
        if self._index < len(self._violations) - 1:
            self._index += 1
            self._refresh()

    def _on_jump(self) -> None:
        v = self._violations[self._index]
        if v.situation_number is not None:
            self.jump_to_situation.emit(v.situation_number)
            self.accept()
