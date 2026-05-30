"""Situation edit panel — the bottom half of the game's profile editor.

The visual layout lives in `forms/situation_panel.ui` (editable in Qt Designer).
This class wires Python behavior onto the loaded form: bucket selection →
situation number, edits → `situation_changed` signal, COPY button, close button.
"""

from __future__ import annotations

from fbpro98_profile import (
    CategoryWeights,
    Down,
    FieldPosition,
    MinutesRemaining,
    PointSpread,
    ProfileType,
    Situation,
    YardsToGo,
)
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QButtonGroup, QGroupBox, QRadioButton, QWidget

from pnfl_profiler.catalog import CategoryOption, categories_for, category_for_code
from pnfl_profiler.labels import FIELD
from pnfl_profiler.ui.forms.situation_panel_ui import Ui_SituationPanel


class SituationEditPanel(QGroupBox):
    """Edit controls bound to one situation_number."""

    situation_changed = Signal(int, CategoryWeights, bool)
    """(situation_number, weights, stop_clock)"""

    copy_requested = Signal(int)
    """(source_situation_number)"""

    remove_requested = Signal(object)
    """argument is `self`."""

    def __init__(
        self,
        profile_type: ProfileType,
        field_position: FieldPosition,
        situation: Situation,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._profile_type = profile_type
        self._field_position = field_position
        self._categories = categories_for(profile_type)
        self._play_codes: list[int] = [0, 0, 0]
        self._suppress_signals = True

        self.ui = Ui_SituationPanel()
        self.ui.setupUi(self)

        self._minutes_radios: dict[MinutesRemaining, QRadioButton] = {
            MinutesRemaining.OVER_FIVE: self.ui.radioMinutesOverFive,
            MinutesRemaining.TWO_TO_FIVE: self.ui.radioMinutesTwoToFive,
            MinutesRemaining.ONE_TO_TWO: self.ui.radioMinutesOneToTwo,
            MinutesRemaining.FIFTEEN_SEC_TO_ONE: self.ui.radioMinutesFifteenSecToOne,
            MinutesRemaining.ZERO_TO_FIFTEEN_SEC: self.ui.radioMinutesZeroToFifteenSec,
        }
        self._down_radios: dict[Down, QRadioButton] = {
            Down.FIRST: self.ui.radioDownFirst,
            Down.SECOND: self.ui.radioDownSecond,
            Down.THIRD: self.ui.radioDownThird,
            Down.Fourth: self.ui.radioDownFourth,
        }
        self._yards_radios: dict[YardsToGo, QRadioButton] = {
            YardsToGo.ZERO_TO_ONE: self.ui.radioYardsZeroToOne,
            YardsToGo.TWO_TO_FIVE: self.ui.radioYardsTwoToFive,
            YardsToGo.SIX_TO_TEN: self.ui.radioYardsSixToTen,
            YardsToGo.OVER_TEN: self.ui.radioYardsOverTen,
        }
        self._spread_radios: dict[PointSpread, QRadioButton] = {
            PointSpread.AHEAD_8_OR_MORE: self.ui.radioSpreadAheadEightOrMore,
            PointSpread.AHEAD_4_TO_7: self.ui.radioSpreadAheadFourToSeven,
            PointSpread.AHEAD_1_TO_3: self.ui.radioSpreadAheadOneToThree,
            PointSpread.TIED: self.ui.radioSpreadTied,
            PointSpread.BEHIND_1_TO_3: self.ui.radioSpreadBehindOneToThree,
            PointSpread.BEHIND_4_TO_7: self.ui.radioSpreadBehindFourToSeven,
            PointSpread.BEHIND_8_OR_MORE: self.ui.radioSpreadBehindEightOrMore,
        }

        # QButtonGroups enforce exclusivity and give us a clean checkedButton API.
        self._minutes_group = self._make_group(self._minutes_radios)
        self._down_group = self._make_group(self._down_radios)
        self._yards_group = self._make_group(self._yards_radios)
        self._spread_group = self._make_group(self._spread_radios)

        self._combos = (
            self.ui.categoryCombo1,
            self.ui.categoryCombo2,
            self.ui.categoryCombo3,
        )
        self._spins = (self.ui.weightSpin1, self.ui.weightSpin2, self.ui.weightSpin3)
        self._percent_labels = (
            self.ui.percentLabel1,
            self.ui.percentLabel2,
            self.ui.percentLabel3,
        )
        for combo in self._combos:
            for opt in self._categories:
                combo.addItem(opt.label, opt)
        self.ui.fieldPositionLabel.setText(f"Field Position: {FIELD[field_position]}")

        # Disable structurally-invalid yards when pinned to <DEF 5.
        if field_position == FieldPosition.INSIDE_DEF_5:
            self._yards_radios[YardsToGo.SIX_TO_TEN].setEnabled(False)
            self._yards_radios[YardsToGo.OVER_TEN].setEnabled(False)

        self._wire_signals()
        self.set_situation(situation)
        self._suppress_signals = False

    # ---------------------------------------------------------------
    # Wiring
    # ---------------------------------------------------------------

    def _make_group(self, radios: dict) -> QButtonGroup:
        group = QButtonGroup(self)
        for rb in radios.values():
            group.addButton(rb)
        return group

    def _wire_signals(self) -> None:
        self.ui.stopClockCheck.toggled.connect(self._on_edit_committed)
        self.ui.closeButton.clicked.connect(lambda: self.remove_requested.emit(self))
        self.ui.copyButton.clicked.connect(self._on_copy_clicked)
        for group in (
            self._minutes_group,
            self._down_group,
            self._yards_group,
            self._spread_group,
        ):
            group.buttonClicked.connect(lambda *_: self._on_edit_committed())
        for i, combo in enumerate(self._combos):
            combo.currentIndexChanged.connect(
                lambda _ix, row=i: self._on_category_changed(row)
            )
        for spin in self._spins:
            spin.valueChanged.connect(self._on_weight_changed)

    # ---------------------------------------------------------------
    # State sync
    # ---------------------------------------------------------------

    def set_situation(self, situation: Situation) -> None:
        prev_suppress = self._suppress_signals
        self._suppress_signals = True
        try:
            self.ui.situationNumberLabel.setText(str(situation.situation_number))
            self.ui.stopClockCheck.setChecked(situation.stop_clock)
            self._minutes_radios[situation.minutes_remaining].setChecked(True)
            self._down_radios[situation.down].setChecked(True)
            self._yards_radios[situation.yards_to_go].setChecked(True)
            self._spread_radios[situation.point_spread].setChecked(True)

            cw = situation.category_weights
            rows = (
                (cw.play_category1, cw.weight1),
                (cw.play_category2, cw.weight2),
                (cw.play_category3, cw.weight3),
            )
            for i, (code, weight) in enumerate(rows):
                self._play_codes[i] = code
                option = category_for_code(code, self._profile_type)
                if option is not None:
                    self._combos[i].setCurrentIndex(self._categories.index(option))
                else:
                    self._combos[i].setCurrentIndex(0)
                self._spins[i].setValue(weight)
            self._recompute_percents()
        finally:
            self._suppress_signals = prev_suppress

    @property
    def field_position(self) -> FieldPosition:
        return self._field_position

    def current_situation_number(self) -> int:
        return self._compute_situation_number()

    # ---------------------------------------------------------------
    # Event handlers
    # ---------------------------------------------------------------

    def _on_category_changed(self, row: int) -> None:
        if self._suppress_signals:
            return
        option: CategoryOption = self._combos[row].currentData()
        self._play_codes[row] = option.default_code
        self._on_edit_committed()

    def _on_weight_changed(self, _value: int) -> None:
        if self._suppress_signals:
            return
        self._recompute_percents()
        self._on_edit_committed()

    def _on_copy_clicked(self) -> None:
        try:
            self.copy_requested.emit(self._compute_situation_number())
        except ValueError:
            return

    def _on_edit_committed(self) -> None:
        if self._suppress_signals:
            return
        try:
            n = self._compute_situation_number()
        except ValueError:
            return
        weights = self._build_weights()
        self.situation_changed.emit(n, weights, self.ui.stopClockCheck.isChecked())

    # ---------------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------------

    def _selected_key(self, radios: dict):
        for key, rb in radios.items():
            if rb.isChecked():
                return key
        return None

    def _compute_situation_number(self) -> int:
        minutes = self._selected_key(self._minutes_radios)
        down = self._selected_key(self._down_radios)
        yards = self._selected_key(self._yards_radios)
        spread = self._selected_key(self._spread_radios)
        if minutes is None or down is None or yards is None or spread is None:
            raise ValueError("incomplete situation selection")
        assert isinstance(minutes, MinutesRemaining)
        assert isinstance(down, Down)
        assert isinstance(yards, YardsToGo)
        assert isinstance(spread, PointSpread)
        n = Situation._situation_number_from_game_state(
            minutes, down, yards, self._field_position, spread
        )
        self.ui.situationNumberLabel.setText(str(n))
        return n

    def _build_weights(self) -> CategoryWeights:
        return CategoryWeights(
            play_category1=self._play_codes[0],
            weight1=self._spins[0].value(),
            play_category2=self._play_codes[1],
            weight2=self._spins[1].value(),
            play_category3=self._play_codes[2],
            weight3=self._spins[2].value(),
        )

    def _recompute_percents(self) -> None:
        total = sum(spin.value() for spin in self._spins)
        for spin, label in zip(self._spins, self._percent_labels, strict=True):
            if total <= 0:
                label.setText("0%")
            else:
                label.setText(f"{round(spin.value() * 100 / total)}%")
