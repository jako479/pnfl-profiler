"""PNFL-allowed play categories per side.

Joins three sources that live in separate libraries:

- **PRF profile codes** — integers in the `.prf` file (0x00..0x1A); the
  canonical Python constants are in `pnfl_profile.rules`.
- **PNFL-allowed subset** — the names in `fbpro98_play.model.OFFENSIVE_CATEGORIES`
  and `DEFENSIVE_CATEGORIES`, minus "User Specific". 13 offense, 10 defense.
- **Display labels** — ALL-CAPS text matching the in-game UI buttons (transcribed
  from `research/screenshots/`).

The defense side collapses the three directional pass codes (0x07..0x0F) into
single "PASS LONG" / "PASS MEDIUM" / "PASS SHORT" labels. When the user picks
"PASS LONG" on defense, the canonical MIDDLE variant is written; loaded codes
already in the file are preserved by `code_to_category` keeping the dropdown's
selection consistent without changing the byte.
"""

from __future__ import annotations

from dataclasses import dataclass

from fbpro98_profile import ProfileType
from pnfl_profile.rules import (
    GOAL_LINE_PASS,
    GOAL_LINE_RUN,
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
    RAZZLE_DAZZLE_RUN,
    RUN_LEFT,
    RUN_MIDDLE,
    RUN_RIGHT,
)


@dataclass(frozen=True, slots=True)
class CategoryOption:
    """One row in the play-category dropdown.

    `default_code` is the PRF code written when the user picks this option fresh.
    `codes` lists every PRF code that displays under this label (for defense,
    a single label like "PASS LONG" covers three direction-variant codes).
    """

    label: str
    default_code: int
    codes: frozenset[int]


# Order mirrors the PNFL-allowed set in `fbpro98_play.model.OFFENSIVE_CATEGORIES`,
# rearranged for the dropdown menu (runs first, then pass-short, pass-medium,
# pass-long-right, razzle-dazzle, goal line).
OFFENSE_CATEGORIES: tuple[CategoryOption, ...] = (
    CategoryOption("RUN LEFT", RUN_LEFT, frozenset({RUN_LEFT})),
    CategoryOption("RUN MIDDLE", RUN_MIDDLE, frozenset({RUN_MIDDLE})),
    CategoryOption("RUN RIGHT", RUN_RIGHT, frozenset({RUN_RIGHT})),
    CategoryOption("PASS SHORT LEFT", PASS_SHORT_LEFT, frozenset({PASS_SHORT_LEFT})),
    CategoryOption(
        "PASS SHORT MIDDLE", PASS_SHORT_MIDDLE, frozenset({PASS_SHORT_MIDDLE})
    ),
    CategoryOption("PASS SHORT RIGHT", PASS_SHORT_RIGHT, frozenset({PASS_SHORT_RIGHT})),
    CategoryOption("PASS MEDIUM LEFT", PASS_MEDIUM_LEFT, frozenset({PASS_MEDIUM_LEFT})),
    CategoryOption(
        "PASS MEDIUM MIDDLE", PASS_MEDIUM_MIDDLE, frozenset({PASS_MEDIUM_MIDDLE})
    ),
    CategoryOption(
        "PASS MEDIUM RIGHT", PASS_MEDIUM_RIGHT, frozenset({PASS_MEDIUM_RIGHT})
    ),
    CategoryOption("PASS LONG RIGHT", PASS_LONG_RIGHT, frozenset({PASS_LONG_RIGHT})),
    CategoryOption(
        "RAZZLE DAZZLE PASS", RAZZLE_DAZZLE_PASS, frozenset({RAZZLE_DAZZLE_PASS})
    ),
    CategoryOption("GOAL LINE RUN", GOAL_LINE_RUN, frozenset({GOAL_LINE_RUN})),
    CategoryOption("GOAL LINE PASS", GOAL_LINE_PASS, frozenset({GOAL_LINE_PASS})),
)

# Defense PNFL-allowed set with directional pass codes collapsed.
DEFENSE_CATEGORIES: tuple[CategoryOption, ...] = (
    CategoryOption("RUN LEFT", RUN_LEFT, frozenset({RUN_LEFT})),
    CategoryOption("RUN MIDDLE", RUN_MIDDLE, frozenset({RUN_MIDDLE})),
    CategoryOption("RUN RIGHT", RUN_RIGHT, frozenset({RUN_RIGHT})),
    CategoryOption(
        "RAZZLE DAZZLE RUN", RAZZLE_DAZZLE_RUN, frozenset({RAZZLE_DAZZLE_RUN})
    ),
    CategoryOption(
        "PASS SHORT",
        PASS_SHORT_MIDDLE,
        frozenset({PASS_SHORT_LEFT, PASS_SHORT_MIDDLE, PASS_SHORT_RIGHT}),
    ),
    CategoryOption(
        "PASS MEDIUM",
        PASS_MEDIUM_MIDDLE,
        frozenset({PASS_MEDIUM_LEFT, PASS_MEDIUM_MIDDLE, PASS_MEDIUM_RIGHT}),
    ),
    CategoryOption(
        "PASS LONG",
        PASS_LONG_MIDDLE,
        frozenset({PASS_LONG_LEFT, PASS_LONG_MIDDLE, PASS_LONG_RIGHT}),
    ),
    CategoryOption(
        "RAZZLE DAZZLE PASS", RAZZLE_DAZZLE_PASS, frozenset({RAZZLE_DAZZLE_PASS})
    ),
    CategoryOption("GOAL LINE RUN", GOAL_LINE_RUN, frozenset({GOAL_LINE_RUN})),
    CategoryOption("GOAL LINE PASS", GOAL_LINE_PASS, frozenset({GOAL_LINE_PASS})),
)


def categories_for(profile_type: ProfileType) -> tuple[CategoryOption, ...]:
    if profile_type == ProfileType.OFFENSE:
        return OFFENSE_CATEGORIES
    return DEFENSE_CATEGORIES


def category_for_code(code: int, profile_type: ProfileType) -> CategoryOption | None:
    """Return the dropdown option whose `codes` set covers `code`.

    Returns None for PRF codes that exist in the file format but aren't in
    PNFL's allowed set (e.g., PUNT, FIELD_GOAL_PAT in a regular situation
    record). UI callers should fall back gracefully — typically by showing
    the raw code or the first option — and surface it as a violation when
    the user runs Check Profile.
    """
    for option in categories_for(profile_type):
        if code in option.codes:
            return option
    return None
