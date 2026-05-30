r"""Qt Designer `.ui` files and their `pyside6-uic`-generated Python wrappers.

Brian edits the `.ui` files in `pyside6-designer`. After saving an edit, run::

    pyside6-uic forms\situation_panel.ui -o forms\situation_panel_ui.py

(repeat for any other edited form). The `*_ui.py` files are checked in so the
package works without a build step; treat them as generated artifacts — don't
hand-edit.
"""
