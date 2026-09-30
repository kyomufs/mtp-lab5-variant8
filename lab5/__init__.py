"""Lab 5: visual programming tasks (Tkinter, PyQt5), variant 8.

Every submodule keeps its toolkit imports lazy, so the whole package
can be imported on a machine without a display and without PyQt5.
"""

from lab5.file_dialog import build_file_window, choose_file
from lab5.listbox_app import build_listbox_window, selected_item
from lab5.multiwindow import (
    build_main_window,
    child_window_title,
    open_child_window,
)
from lab5.notes import NotesModel
from lab5.notes_app import build_notes_window
from lab5.pyqt_hello import build_window

__all__ = [
    "NotesModel",
    "build_file_window",
    "build_listbox_window",
    "build_main_window",
    "build_notes_window",
    "build_window",
    "child_window_title",
    "choose_file",
    "open_child_window",
    "selected_item",
]
