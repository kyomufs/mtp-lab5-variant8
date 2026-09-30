"""Advanced task 8: program that opens several windows."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import tkinter as tk

_child_window_count = 0


def child_window_title(index: int) -> str:
    """Return the title for child window number ``index``.

    Child windows are numbered from one in the order they were
    opened.

    Args:
        index: one-based window number.

    Returns:
        The title string for that window.

    Raises:
        ValueError: if ``index`` is less than one.
    """
    if index < 1:
        raise ValueError("window index must be >= 1")
    return f"Child window {index}"


def build_main_window(
    root: tk.Misc, open_child: Callable[[], None]
) -> tk.Button:
    """Create the main window button inside ``root``.

    Args:
        root: parent widget for the button.
        open_child: callback that opens a child window.

    Returns:
        The created button widget.
    """
    import tkinter as tk

    button = tk.Button(root, text="Открыть окно", command=open_child)
    button.pack()
    return button


def open_child_window(parent: tk.Misc) -> tk.Toplevel:
    """Open a child window attached to ``parent``.

    The child holds a text entry and a button that closes it. Each
    child gets a unique title taken from
    :func:`child_window_title`, counted from one for the whole
    process.

    Args:
        parent: widget the new window belongs to.

    Returns:
        The created ``Toplevel`` window.
    """
    global _child_window_count
    import tkinter as tk

    _child_window_count += 1
    child = tk.Toplevel(parent)
    child.title(child_window_title(_child_window_count))
    entry = tk.Entry(child)
    entry.pack()
    button = tk.Button(child, text="Close", command=child.destroy)
    button.pack()
    return child
