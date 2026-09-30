"""Advanced task 1: Tkinter window for the notes program."""

from __future__ import annotations

from typing import TYPE_CHECKING

from lab5.notes import NotesModel

if TYPE_CHECKING:
    import tkinter as tk


def build_notes_window(root: tk.Misc, model: NotesModel) -> tk.Listbox:
    """Create the notes UI (entry, button, list) inside ``root``.

    The listbox is pre-filled with ``model.all()``. Clicking the
    "Сохранить" button appends the trimmed entry text to ``model``
    and to the listbox, then clears the entry; an empty entry is
    ignored. tkinter is imported lazily, so the module loads
    without a display.

    Args:
        root: parent widget for the entry, the button and the list.
        model: storage the button writes to.

    Returns:
        The listbox showing the notes.
    """
    import tkinter as tk

    entry = tk.Entry(root)
    listbox = tk.Listbox(root)
    for note in model.all():
        listbox.insert(tk.END, note)

    def handle_save() -> None:
        text = entry.get().strip()
        if not text:
            return
        model.add(text)
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

    button = tk.Button(root, text="Сохранить", command=handle_save)
    entry.pack(fill=tk.X)
    button.pack()
    listbox.pack(fill=tk.BOTH, expand=True)
    return listbox
