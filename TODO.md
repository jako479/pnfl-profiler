## Consolidate play-category name lists

`pnfl-profiler` maintains a local table mapping PNFL-allowed play-category names to profile codes for the dropdowns. The PNFL-allowed *name list* duplicates what's already in [fbpro98-play/model.py:13](../fbpro98-play/src/fbpro98_play/model.py#L13)'s `OFFENSIVE_CATEGORIES` / `DEFENSIVE_CATEGORIES`; the *profile codes* come from [pnfl-profile/rules.py:26-52](../pnfl-profile/src/pnfl_profile/rules.py#L26-L52).

Pick one canonical home for the PNFL-allowed category list (likely alongside the codes in `pnfl-profile` or `fbpro98-profile`) and have both `pnfl-profiler` and `fbpro98-play` reference it. The current duplication risks drift if the PNFL-allowed set changes.
