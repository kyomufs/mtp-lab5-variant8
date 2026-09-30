"""Task 8 (medium): file open dialog."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import tkinter as tk


def choose_file(dialog: Callable[[], str] | None = None) -> str | None:
    """Return the path selected in a file dialog.

    Args:
        dialog: zero-argument callable returning a path. When it is
            ``None``, ``tkinter.filedialog.askopenfilename`` is used.
            tkinter is imported lazily, so the module loads without
            a display.

    Returns:
        The selected path, or ``None`` when the dialog was cancelled
        (empty string).
    """
    picker = dialog
    if picker is None:
        from tkinter import filedialog

        picker = filedialog.askopenfilename
    path = picker()
    return path if path else None


def build_file_window(
    root: tk.Misc, chooser: Callable[[], str | None]
) -> tk.Button:
    """Create a button that asks ``chooser`` for a file path.

    The result is shown in a label under the button: the chosen path
    or ``"No file selected"`` after a cancellation.

    Args:
        root: parent widget for the button and the label.
        chooser: callable returning a path or ``None``.

    Returns:
        The created button widget.
    """
    import tkinter as tk

    status = tk.Label(root, text="No file selected")

    def handle_click() -> None:
        path = chooser()
        status.config(text=path if path else "No file selected")

    button = tk.Button(root, text="Open file...", command=handle_click)
    button.pack()
    status.pack()
    return button
