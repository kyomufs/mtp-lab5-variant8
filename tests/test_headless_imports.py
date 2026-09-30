"""Smoke test: every lab5 module imports without a GUI toolkit."""

import importlib
import sys
import unittest

MODULES = [
    "lab5",
    "lab5.file_dialog",
    "lab5.listbox_app",
    "lab5.multiwindow",
    "lab5.notes",
    "lab5.notes_app",
    "lab5.pyqt_hello",
]


class HeadlessImportTests(unittest.TestCase):
    """Importing the package must not touch tkinter or PyQt5."""

    def test_every_module_imports(self) -> None:
        """Each module of the package loads on a headless machine."""
        for name in MODULES:
            with self.subTest(module=name):
                module = importlib.import_module(name)
                self.assertIsNotNone(module)

    def test_toolkits_stay_unimported(self) -> None:
        """No test triggered an eager tkinter or PyQt5 import."""
        for name in ("tkinter", "PyQt5"):
            with self.subTest(toolkit=name):
                self.assertNotIn(name, sys.modules)


if __name__ == "__main__":
    unittest.main()
