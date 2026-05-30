"""Display strings for situation buckets, taken from the in-game UI.

Labels come from `research/screenshots/offense_edit.png` and `defense_edit.png`
exactly as the game shows them. They are NOT the spec's UPPER_SNAKE identifiers
(those are programmer-facing only).
"""

from __future__ import annotations

from fbpro98_profile import (
    Down,
    FieldPosition,
    MinutesRemaining,
    PointSpread,
    YardsToGo,
)

MINUTES: dict[MinutesRemaining, str] = {
    MinutesRemaining.OVER_FIVE: ">5",
    MinutesRemaining.TWO_TO_FIVE: ">2-5",
    MinutesRemaining.ONE_TO_TWO: ">1-2",
    MinutesRemaining.FIFTEEN_SEC_TO_ONE: ">:15-1",
    MinutesRemaining.ZERO_TO_FIFTEEN_SEC: "0-:15",
}

DOWN: dict[Down, str] = {
    Down.FIRST: "1",
    Down.SECOND: "2",
    Down.THIRD: "3",
    Down.Fourth: "4",
}

YARDS: dict[YardsToGo, str] = {
    YardsToGo.ZERO_TO_ONE: "0-1",
    YardsToGo.TWO_TO_FIVE: "2-5",
    YardsToGo.SIX_TO_TEN: "6-10",
    YardsToGo.OVER_TEN: ">10",
}

FIELD: dict[FieldPosition, str] = {
    FieldPosition.INSIDE_DEF_5: "<DEF 5",
    FieldPosition.DEF_5_TO_DEF_35: "DEF 5 - DEF 35",
    FieldPosition.DEF_35_TO_OFF_35: "DEF 35 - OFF 35",
    FieldPosition.OFF_35_TO_OFF_5: "OFF 35 - OFF 5",
    FieldPosition.INSIDE_OFF_5: "<OFF 5",
}

SPREAD: dict[PointSpread, str] = {
    PointSpread.AHEAD_8_OR_MORE: "Ahead by 8+",
    PointSpread.AHEAD_4_TO_7: "Ahead by 4-7",
    PointSpread.AHEAD_1_TO_3: "Ahead by 1-3",
    PointSpread.TIED: "Tied",
    PointSpread.BEHIND_1_TO_3: "Behind by 1-3",
    PointSpread.BEHIND_4_TO_7: "Behind by 4-7",
    PointSpread.BEHIND_8_OR_MORE: "Behind by 8+",
}
