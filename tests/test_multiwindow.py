"""Tests for the multi-window program (advanced no.8)."""

import unittest

import lab5.multiwindow
from lab5.multiwindow import child_window_title


class ChildWindowTitleTests(unittest.TestCase):
    """Checks for :func:`lab5.multiwindow.child_window_title`."""

    def test_module_imports_without_display(self) -> None:
        """The module imports headless and exposes both builders."""
        self.assertTrue(callable(lab5.multiwindow.build_main_window))
        self.assertTrue(callable(lab5.multiwindow.open_child_window))

    def test_first_window_title(self) -> None:
        """Window number one gets the base title."""
        self.assertEqual(child_window_title(1), "Child window 1")

    def test_later_window_title(self) -> None:
        """The index is embedded in the title verbatim."""
        self.assertEqual(child_window_title(7), "Child window 7")

    def test_index_below_one_is_rejected(self) -> None:
        """Zero and negative indexes are not valid window numbers."""
        with self.assertRaises(ValueError):
            child_window_title(0)
        with self.assertRaises(ValueError):
            child_window_title(-3)


if __name__ == "__main__":
    unittest.main()
