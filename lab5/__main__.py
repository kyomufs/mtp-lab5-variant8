"""Demo entry point: run ``python -m lab5``."""

import os

from lab5.listbox_app import build_listbox_window


def has_display() -> bool:
    """Return ``True`` when the ``DISPLAY`` variable is set."""
    return bool(os.environ.get("DISPLAY"))


def print_task_list() -> None:
    """Print every task of the variant under its header."""
    print("Medium tasks")
    print("  No.4 listbox and item selection -> lab5.listbox_app")
    print("  No.8 file open dialog -> lab5.file_dialog")
    print("  No.10 simplest GUI on PyQt5 -> lab5.pyqt_hello")
    print("Advanced tasks")
    print("  No.1 notes program -> lab5.notes, lab5.notes_app")
    print("  No.8 multi-window program -> lab5.multiwindow")


def run_gui_demo() -> None:
    """Open the listbox demo window when a display is reachable."""
    try:
        import tkinter as tk
    except ImportError:
        print("tkinter is not available; GUI demo skipped")
        return
    root = tk.Tk()
    root.title("Lab 5 variant 8: listbox demo")
    items = ["alpha", "beta", "gamma"]
    build_listbox_window(
        root, items, lambda value: print("selected:", value)
    )
    root.mainloop()


def main() -> None:
    """Print the task list and start the GUI demo if possible."""
    print_task_list()
    if has_display():
        run_gui_demo()
    else:
        print("No display available")


if __name__ == "__main__":
    main()
