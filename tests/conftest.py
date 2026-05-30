"""Shared fixtures: copy the read-only `.prf` fixtures to tmp_path before tests
that may mutate them through `ProfileSession.save`.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture
def tst_off_path(tmp_path: Path) -> Path:
    dest = tmp_path / "TST-OFF1.prf"
    shutil.copy(DATA_DIR / "TST-OFF1.prf", dest)
    return dest


@pytest.fixture
def tst_def_path(tmp_path: Path) -> Path:
    dest = tmp_path / "TST-DEF1.prf"
    shutil.copy(DATA_DIR / "TST-DEF1.prf", dest)
    return dest
