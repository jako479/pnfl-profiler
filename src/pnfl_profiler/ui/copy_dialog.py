"""COPY dialog — destination buckets + Plays/Clock mask.

Layout lives in `forms/copy_dialog.ui` (editable in Qt Designer). This class
expands the checked buckets into situation numbers and exposes the result.
"""

from __future__ import annotations

from itertools import product

from fbpro98_profile import (
    Down,
    FieldPosition,
    MinutesRemaining,
    PointSpread,
    Situation,
    YardsToGo,
)
from PySide6.QtWidgets import QCheckBox, QDialog, QDialogButtonBox, QWidget

from pnfl_profiler.ui.forms.copy_dialog_ui import Ui_CopyDialog


class CopyDialog(QDialog):
    def __init__(
        self, source_situation_number: int, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self._source = source_situation_number

        self.ui = Ui_CopyDialog()
        self.ui.setupUi(self)

        self._minutes_boxes: dict[MinutesRemaining, QCheckBox] = {
            MinutesRemaining.OVER_FIVE: self.ui.checkMinutesOverFive,
            MinutesRemaining.TWO_TO_FIVE: self.ui.checkMinutesTwoToFive,
            MinutesRemaining.ONE_TO_TWO: self.ui.checkMinutesOneToTwo,
            MinutesRemaining.FIFTEEN_SEC_TO_ONE: self.ui.checkMinutesFifteenSecToOne,
            MinutesRemaining.ZERO_TO_FIFTEEN_SEC: self.ui.checkMinutesZeroToFifteenSec,
        }
        self._down_boxes: dict[Down, QCheckBox] = {
            Down.FIRST: self.ui.checkDownFirst,
            Down.SECOND: self.ui.checkDownSecond,
            Down.THIRD: self.ui.checkDownThird,
            Down.Fourth: self.ui.checkDownFourth,
        }
        self._yards_boxes: dict[YardsToGo, QCheckBox] = {
            YardsToGo.ZERO_TO_ONE: self.ui.checkYardsZeroToOne,
            YardsToGo.TWO_TO_FIVE: self.ui.checkYardsTwoToFive,
            YardsToGo.SIX_TO_TEN: self.ui.checkYardsSixToTen,
            YardsToGo.OVER_TEN: self.ui.checkYardsOverTen,
        }
        self._field_boxes: dict[FieldPosition, QCheckBox] = {
            FieldPosition.INSIDE_DEF_5: self.ui.checkFieldInsideDef5,
            FieldPosition.DEF_5_TO_DEF_35: self.ui.checkFieldDef5ToDef35,
            FieldPosition.DEF_35_TO_OFF_35: self.ui.checkFieldDef35ToOff35,
            FieldPosition.OFF_35_TO_OFF_5: self.ui.checkFieldOff35ToOff5,
            FieldPosition.INSIDE_OFF_5: self.ui.checkFieldInsideOff5,
        }
        self._spread_boxes: dict[PointSpread, QCheckBox] = {
            PointSpread.AHEAD_8_OR_MORE: self.ui.checkSpreadAheadEightOrMore,
            PointSpread.AHEAD_4_TO_7: self.ui.checkSpreadAheadFourToSeven,
            PointSpread.AHEAD_1_TO_3: self.ui.checkSpreadAheadOneToThree,
            PointSpread.TIED: self.ui.checkSpreadTied,
            PointSpread.BEHIND_1_TO_3: self.ui.checkSpreadBehindOneToThree,
            PointSpread.BEHIND_4_TO_7: self.ui.checkSpreadBehindFourToSeven,
            PointSpread.BEHIND_8_OR_MORE: self.ui.checkSpreadBehindEightOrMore,
        }

        for cb in (
            *self._minutes_boxes.values(),
            *self._down_boxes.values(),
            *self._yards_boxes.values(),
            *self._field_boxes.values(),
            *self._spread_boxes.values(),
            self.ui.checkPlays,
            self.ui.checkClock,
        ):
            cb.toggled.connect(self._recompute_count)

        self._ok_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        self._ok_button.setEnabled(False)
        self._recompute_count()

    # ---------------------------------------------------------------
    # Count + accessors
    # ---------------------------------------------------------------

    def _recompute_count(self) -> None:
        targets = self.destination_situation_numbers()
        valid = [n for n in targets if n != self._source]
        self.ui.countLabel.setText(f"Situations: {len(valid)}")
        any_kind = self.ui.checkPlays.isChecked() or self.ui.checkClock.isChecked()
        self._ok_button.setEnabled(bool(valid) and any_kind)

    def destination_situation_numbers(self) -> tuple[int, ...]:
        """Expand checked buckets into situation_numbers; filter invalid combos."""
        minutes = [v for v, cb in self._minutes_boxes.items() if cb.isChecked()]
        downs = [v for v, cb in self._down_boxes.items() if cb.isChecked()]
        yards = [v for v, cb in self._yards_boxes.items() if cb.isChecked()]
        fields = [v for v, cb in self._field_boxes.items() if cb.isChecked()]
        spreads = [v for v, cb in self._spread_boxes.items() if cb.isChecked()]
        if not all((minutes, downs, yards, fields, spreads)):
            return ()
        out: list[int] = []
        for m, d, y, f, s in product(minutes, downs, yards, fields, spreads):
            try:
                out.append(Situation._situation_number_from_game_state(m, d, y, f, s))
            except ValueError:
                continue
        return tuple(out)

    def copy_plays(self) -> bool:
        return self.ui.checkPlays.isChecked()

    def copy_clock(self) -> bool:
        return self.ui.checkClock.isChecked()
