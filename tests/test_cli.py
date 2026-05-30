"""CLI smoke tests — argument parsing and file-not-found exit codes."""

from __future__ import annotations

from pathlib import Path

import pytest

from pnfl_profiler.cli import build_parser, main


def test_parser_accepts_no_args() -> None:
    args = build_parser().parse_args([])
    assert args.profile is None


def test_parser_accepts_path() -> None:
    args = build_parser().parse_args(["foo.prf"])
    assert args.profile == Path("foo.prf")


def test_main_returns_2_for_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "does_not_exist.prf"
    assert main([str(missing)]) == 2


def test_help_exits(monkeypatch: pytest.MonkeyPatch) -> None:
    with pytest.raises(SystemExit) as excinfo:
        build_parser().parse_args(["-h"])
    assert excinfo.value.code == 0
