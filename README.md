# pnfl-profiler

PySide6 desktop editor for Front Page Sports Football Pro '98 coaching profiles (`.prf`). Replaces the in-game profile editor with a Python-native UI bound to `pnfl-profile` for PNFL rule validation.

For internal design, see [ARCHITECTURE.md](ARCHITECTURE.md). For use-case walk-throughs and the call stack down into the data libraries, see [pnfl-docs/Design/profiler-use-cases.md](../pnfl-docs/Design/profiler-use-cases.md).

## Setup

```powershell
py -3.13 -m venv .venv
.venv\Scripts\activate
py -m pip install -e ..\fbpro98-profile
py -m pip install -e ..\pnfl-profile
py -m pip install -e ".[dev]"
```

## Usage

Launch via the `pnfl` umbrella (after installing `pnfl` from the sibling repo):

```powershell
pnfl edit-profile path\to\DEN-OFF1.prf
```

Or directly:

```powershell
py -m pnfl_profiler path\to\DEN-OFF1.prf
```

## Editing the UI

Every UI piece is a Qt Designer `.ui` file under `src/pnfl_profiler/ui/forms/`. Python files in `src/pnfl_profiler/ui/` hold only behavior (signals, model glue, dynamic widget insertion).

Open a form in Designer:

```powershell
pyside6-designer src\pnfl_profiler\ui\forms\main_window.ui
pyside6-designer src\pnfl_profiler\ui\forms\field_position_pane.ui
pyside6-designer src\pnfl_profiler\ui\forms\situation_panel.ui
pyside6-designer src\pnfl_profiler\ui\forms\copy_dialog.ui
pyside6-designer src\pnfl_profiler\ui\forms\check_profile_dialog.ui
```

After saving an edit, regenerate that form's Python wrapper:

```powershell
pyside6-uic src\pnfl_profiler\ui\forms\main_window.ui          -o src\pnfl_profiler\ui\forms\main_window_ui.py
pyside6-uic src\pnfl_profiler\ui\forms\field_position_pane.ui  -o src\pnfl_profiler\ui\forms\field_position_pane_ui.py
pyside6-uic src\pnfl_profiler\ui\forms\situation_panel.ui      -o src\pnfl_profiler\ui\forms\situation_panel_ui.py
pyside6-uic src\pnfl_profiler\ui\forms\copy_dialog.ui          -o src\pnfl_profiler\ui\forms\copy_dialog_ui.py
pyside6-uic src\pnfl_profiler\ui\forms\check_profile_dialog.ui -o src\pnfl_profiler\ui\forms\check_profile_dialog_ui.py
```

The `*_ui.py` files are checked in (generated artifacts, don't hand-edit).

## Scope (v1)

Edit per situation: three play categories, three weights, and the stop-clock flag. Bulk-apply one situation's settings to others through a COPY dialog. Run PNFL `Check Profile` to walk violations. Out of v1 scope: PAT editor, substitution percentages, field-goal range. Audibles are always saved off.

## Testing

```powershell
pytest
```

## Building a Release

Ships these artifacts to the umbrella bundle:

- Python wheel (built by `pnfl/scripts/build_release.py`)

Distributed as part of the [`pnfl`](../pnfl) umbrella CLI.
