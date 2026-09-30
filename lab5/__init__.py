"""Lab 5: visual programming tasks (Tkinter, PyQt5), variant 8.

Every submodule keeps its toolkit imports lazy, so the whole package
can be imported on a machine without a display and without PyQt5.
"""

from lab5.file_dialog import build_file_window, choose_file
from lab5.listbox_app import build_listbox_window, selected_item

__all__ = [
    "build_file_window",
    "build_listbox_window",
    "choose_file",
    "selected_item",
]
