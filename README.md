# INSERT PROJECT NAME HERE

INSERT DESCRIPTION HERE

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
# pip install -e ".[dev]"
```

> **When do I need `pip install -e ".[dev]"`?**
>
> The `-e` flag installs a package in "editable" mode — Python reads directly from the
> source files instead of copying them into the venv. This matters in two cases:
>
> 1. **Within this project's own venv:** If the project has a `src/` layout and its own
>    tests import the package (e.g., `from mypackage import something`), `-e` lets the
>    tests see source changes immediately without reinstalling.
>
> 2. **In a consuming project's venv:** If another project depends on this package, you
>    can install it into that project's venv with `pip install -e ..\this-package`. Changes
>    to this package's source files are then picked up immediately by the consuming project.
>    Without `-e`, you'd have to re-run `pip install ..\this-package` after every change.
>
> If you're just running scripts directly (e.g., `python my_script.py`) and nothing else
> imports this project as a package, you don't need it.

## Usage

TODO

## Testing

```bash
pytest
```
