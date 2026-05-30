# pnfl-profiler — Architecture

PySide6 desktop editor for Front Page Sports Football Pro '98 coaching profiles (`.prf`). Replaces the in-game profile editor.

For per-use-case call stacks down into `pnfl-profile` and `fbpro98-profile`, see [pnfl-docs/Design/profiler-use-cases.md](../pnfl-docs/Design/profiler-use-cases.md).

## Module layout

```
src/pnfl_profiler/
├── __init__.py              # re-exports main
├── cli.py                   # argparse + QApplication bootstrap
├── session.py               # ProfileSession — load, edit, save model
├── catalog.py               # PNFL category mapping (PRF code ↔ display label)
├── labels.py                # bucket display strings from the game UI
└── ui/
    ├── main_window.py       # QMainWindow + menu + pane container
    ├── field_position_pane.py
    ├── situation_panel.py   # one situation's edit controls
    ├── copy_dialog.py       # bulk-copy modal
    ├── check_profile_dialog.py
    └── forms/               # Qt Designer .ui files + generated *_ui.py
        ├── main_window.ui
        ├── field_position_pane.ui
        ├── situation_panel.ui
        ├── copy_dialog.ui
        └── check_profile_dialog.ui
```

Every UI piece splits into a `.ui` file (visual layout, edited in `pyside6-designer`) and a `.py` file (behavior, signals, model glue). `main_window.ui` defines the menu structure, shortcuts, and the empty horizontal layout the panes go into; `field_position_pane.ui` defines the header + add button + empty container layout. Python populates the empty layouts at runtime (`paneRowLayout.addWidget(pane)`, `panelContainerLayout.insertWidget(0, panel)`).

After editing any `.ui` file, regenerate its `*_ui.py` wrapper:

```powershell
pyside6-uic src\pnfl_profiler\ui\forms\situation_panel.ui -o src\pnfl_profiler\ui\forms\situation_panel_ui.py
```

The package depends on `pnfl-profile` (which brings `fbpro98-profile` transitively) and `PySide6`. All file I/O and rule logic stay in the data layer; this package is UI + a thin session model.

## What this package does

- Opens a single `.prf` at a time via `PnflProfile.from_file`
- Exposes one situation per `SituationEditPanel`: the three play categories, weights, and stop-clock flag
- Bulk-applies one situation's data to others via a COPY dialog modeled on the game's
- Surfaces PNFL rule violations through a Check Profile dialog over `PnflProfile.validate()`
- Saves via `PnflProfile.save` (validates then writes), and Save-As to a different path
- Forces `Profile.use_audibles = False` on every save (PNFL disallows audibles)

## What this package assumes

- The profile file is parseable by `fbpro98-profile.read_profile` and PNFL-tagged by `PnflProfile.from_file`
- The user has installed `pnfl` and runs the editor as `pnfl edit-profile <path.prf>`
- The host system has a display (no headless mode)

## What this package enforces

- `use_audibles` is `False` on every saved profile, regardless of the loaded value
- Saves go through `PnflProfile.save` so PNFL violations raise `PnflRuleError` before any bytes touch disk
- Edits funnel through `ProfileSession.update_situation` / `copy_situation`, which rebuild the immutable `Profile` via `dataclasses.replace`

## What this package does NOT do

- Edit PAT situations, substitution percentages, or field-goal range — those fields are preserved verbatim from the loaded file and written back unchanged
- Provide any view or toggle for audibles
- Validate the `.prf` byte layout — that lives in `fbpro98-profile`
- Apply PNFL rules — that lives in `pnfl-profile`
- Style the UI — v1 uses default PySide6 widgets only

## Layers

- **`fbpro98-profile`** — owns `.prf` bytes ↔ `Profile`
- **`pnfl-profile`** — wraps `Profile` with `PnflRules`; owns validation
- **`pnfl-profiler.session`** — owns the live `PnflProfile` plus dirty state, path, and the edit / copy / save / Save-As operations
- **`pnfl-profiler.ui`** — owns Qt widgets; calls into `session`; never imports `fbpro98-profile` directly

Immutability flows up: the data layer's frozen dataclasses force the session to rebuild the `Profile` on every edit (via `dataclasses.replace`). The UI never holds a long-lived reference to a `Profile` — it queries `ProfileSession` on demand.

## Edit cycle

1. UI widget emits a change → `MainWindow` slot calls `ProfileSession.update_situation(n, weights, stop_clock)`
2. `ProfileSession` builds a new `Situation` and a new `Profile` via `dataclasses.replace`, then a new `PnflProfile`
3. `ProfileSession` flips the dirty flag and emits `profile_modified`
4. The UI updates whatever derived values it shows (e.g., weight percentages)

COPY follows the same path, but `copy_situation` rebuilds many `Situation` records in one pass before swapping in the new `Profile`.

## Testing

- `tests/test_catalog.py` — PNFL-allowed category mappings vs. `pnfl_profile.rules` constants
- `tests/test_labels.py` — every enum value has a UI label
- `tests/test_session.py` — open / edit / save behavior against `tests/data/TST-OFF1.prf` and `TST-DEF1.prf` copied into `tmp_path`; audibles-forced-off (in-memory + via direct `write_profile`); preservation of `substitutions` / `pat_situations` / `field_goal_range`; COPY destination expansion; `PnflRuleError` on save when the fixture has violations
- `tests/test_cli.py` — `edit-profile` arg parsing, file-not-found exit code, `--help` exit

No UI automation. `pytest-qt` is not a dependency.
