"""Every bucket enum has a UI label."""

from __future__ import annotations

from fbpro98_profile import (
    Down,
    FieldPosition,
    MinutesRemaining,
    PointSpread,
    YardsToGo,
)

from pnfl_profiler.labels import DOWN, FIELD, MINUTES, SPREAD, YARDS


def test_minutes_covers_enum() -> None:
    assert set(MINUTES) == set(MinutesRemaining)


def test_down_covers_enum() -> None:
    assert set(DOWN) == set(Down)


def test_yards_covers_enum() -> None:
    assert set(YARDS) == set(YardsToGo)


def test_field_covers_enum() -> None:
    assert set(FIELD) == set(FieldPosition)


def test_spread_covers_enum() -> None:
    assert set(SPREAD) == set(PointSpread)


def test_no_blank_labels() -> None:
    for mapping in (MINUTES, DOWN, YARDS, FIELD, SPREAD):
        for label in mapping.values():
            assert label.strip()
