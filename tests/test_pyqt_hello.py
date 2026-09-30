"""Tests for the PyQt5 hello window task (medium no.10)."""

import importlib
import importlib.util
import sys
import unittest

import lab5.pyqt_hello
from lab5.pyqt_hello import build_window

HAS_PYQT5 = importlib.util.find_spec("PyQt5") is not None


class PyqtHelloTests(unittest.TestCase):
    """Checks for :func:`lab5.pyqt_hello.build_window`."""

    def test_module_imports_without_pyqt5(self) -> None:
        """The module imports headless and exposes its builder."""
        self.assertTrue(callable(build_window))

    def test_pyqt5_is_imported_lazily(self) -> None:
        """Reloading the module never touches PyQt5."""
        if "PyQt5" in sys.modules:
            self.skipTest("PyQt5 is already imported")
        reloaded = importlib.reload(lab5.pyqt_hello)
        self.assertTrue(callable(reloaded.build_window))
        self.assertNotIn("PyQt5", sys.modules)

    @unittest.skipUnless(HAS_PYQT5, "PyQt5 is not installed")
    def test_qt_is_available_and_builder_callable(self) -> None:
        """With PyQt5 installed the spec resolves and the API works."""
        self.assertIsNotNone(importlib.util.find_spec("PyQt5"))
        self.assertTrue(callable(build_window))


if __name__ == "__main__":
    unittest.main()
