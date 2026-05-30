"""Vertical pane for one field-position bucket.

Static layout (header + add button + empty container + spacer) lives in
`forms/field_position_pane.ui` (editable in Qt Designer). This class wires the
field-position binding, enable/disable on profile load, and dynamic insertion
of `SituationEditPanel` widgets into the container layout.
"""

from __future__ import annotations

from fbpro98_profile import (
    Down,
    FieldPosition,
    MinutesRemaining,
    PointSpread,
    ProfileType,
    Situation,
    YardsToGo,
)
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from pnfl_profiler.labels import FIELD
from pnfl_profiler.ui.forms.field_position_pane_ui import Ui_FieldPositionPane
from pnfl_profiler.ui.situation_panel import SituationEditPanel


class FieldPositionPane(QWidget):
    """One vertical column pinned to a FieldPosition bucket."""

    add_panel_requested = Signal(object)  # FieldPosition
    panel_added = Signal(object)  # SituationEditPanel

    def __init__(
        self, field_position: FieldPosition, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self._field_position = field_position
        self._profile_type: ProfileType | None = None
        self._panels: list[SituationEditPanel] = []

        self.ui = Ui_FieldPositionPane()
        self.ui.setupUi(self)
        self.ui.headerLabel.setText(f"<b>{FIELD[field_position]}</b>")
        self.ui.addButton.clicked.connect(
            lambda: self.add_panel_requested.emit(field_position)
        )

    @property
    def field_position(self) -> FieldPosition:
        return self._field_position

    @property
    def panels(self) -> tuple[SituationEditPanel, ...]:
        return tuple(self._panels)

    def set_profile_type(self, profile_type: ProfileType | None) -> None:
        self._profile_type = profile_type
        self.ui.addButton.setEnabled(profile_type is not None)

    def clear(self) -> None:
        for panel in self._panels:
            self.ui.panelContainerLayout.removeWidget(panel)
            panel.deleteLater()
        self._panels.clear()
        self._profile_type = None
        self.ui.addButton.setEnabled(False)

    def add_panel(self, situation: Situation) -> SituationEditPanel:
        if self._profile_type is None:
            raise RuntimeError("profile type not set; call set_profile_type first")
        panel = SituationEditPanel(
            profile_type=self._profile_type,
            field_position=self._field_position,
            situation=situation,
        )
        panel.remove_requested.connect(self._remove_panel)
        self.ui.panelContainerLayout.insertWidget(0, panel)
        self._panels.insert(0, panel)
        self.panel_added.emit(panel)
        return panel

    def default_situation_number(self) -> int:
        return Situation._situation_number_from_game_state(
            MinutesRemaining.OVER_FIVE,
            Down.FIRST,
            YardsToGo.ZERO_TO_ONE,
            self._field_position,
            PointSpread.AHEAD_8_OR_MORE,
        )

    def find_panel_for_situation(
        self, situation_number: int
    ) -> SituationEditPanel | None:
        for panel in self._panels:
            try:
                if panel.current_situation_number() == situation_number:
                    return panel
            except ValueError:
                continue
        return None

    def _remove_panel(self, panel: SituationEditPanel) -> None:
        if panel in self._panels:
            self._panels.remove(panel)
            self.ui.panelContainerLayout.removeWidget(panel)
            panel.deleteLater()
