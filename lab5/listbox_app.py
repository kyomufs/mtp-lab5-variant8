"""Task 4 (medium): listbox widget and element selection."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import tkinter as tk


def selected_item(items: Sequence[str], index: int) -> str | None:
    """Return the element at ``index`` or ``None`` when out of range.

    Args:
        items: source sequence of strings.
        index: zero-based position; negative positions count as out
            of range.

    Returns:
        ``items[index]`` for ``0 <= index < len(items)``, otherwise
        ``None``.
    """
    if 0 <= index < len(items):
        return items[index]
    return None


def build_listbox_window(
    root: tk.Misc,
    items: Sequence[str],
    on_select: Callable[[str], None],
) -> tk.Listbox:
    """Create a listbox with a caption label inside ``root``.

    Every string from ``items`` is inserted into the listbox. When a
    row is selected, the label below the listbox shows that string
    and ``on_select`` is called with the same value.

    Args:
        root: parent widget for the listbox and the label.
        items: strings displayed in the listbox.
        on_select: callback invoked with the selected string.

    Returns:
        The created listbox widget.
    """
    import tkinter as tk

    listbox = tk.Listbox(root)
    for text in items:
        listbox.insert(tk.END, text)
    label = tk.Label(root, text="Select an item")

    def handle_selection(event: object) -> None:
        selection = listbox.curselection()
        if not selection:
            return
        value = selected_item(items, selection[0])
        if value is None:
            return
        label.config(text=value)
        on_select(value)

    listbox.bind("<<ListboxSelect>>", handle_selection)
    listbox.pack(fill=tk.BOTH, expand=True)
    label.pack(fill=tk.X)
    return listbox
