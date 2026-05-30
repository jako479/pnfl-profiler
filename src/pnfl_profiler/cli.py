"""CLI entry point for the pnfl-profiler editor.

Registered as `pnfl edit-profile` via the `pnfl.commands` entry point group.
"""

from __future__ import annotations

import argparse
import logging
import sys
from collections.abc import Sequence
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMessageBox

PROG = "pnfl edit-profile"
logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=PROG,
        description="PySide6 desktop editor for .prf coaching profiles.",
    )
    parser.add_argument(
        "profile",
        nargs="?",
        type=Path,
        help="Optional .prf path to open on launch.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if args.profile is not None and not args.profile.exists():
        logger.error("%s: %s: file not found", PROG, args.profile)
        return 2

    # Import lazily so `--help` and arg errors don't pay Qt startup cost.
    from pnfl_profiler.session import ProfileSession
    from pnfl_profiler.ui.main_window import MainWindow

    app = QApplication.instance() or QApplication(sys.argv[:1])
    session = ProfileSession()
    window = MainWindow(session)
    window.show()

    if args.profile is not None:
        try:
            session.open(args.profile)
        except Exception as exc:
            QMessageBox.critical(
                window, "Open failed", f"Could not open {args.profile}:\n\n{exc}"
            )

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
