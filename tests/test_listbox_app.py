"""Tests for the listbox selection task (medium no.4)."""

import unittest

import lab5.listbox_app
from lab5.listbox_app import selected_item


class SelectedItemTests(unittest.TestCase):
    """Checks for :func:`lab5.listbox_app.selected_item`."""

    def test_module_imports_without_display(self) -> None:
        """The module imports headless and exposes its builder."""
        self.assertTrue(
            callable(lab5.listbox_app.build_listbox_window)
        )

    def test_existing_index_returns_element(self) -> None:
        """An index inside the sequence returns its element."""
        items = ["alpha", "beta", "gamma"]
        self.assertEqual(selected_item(items, 0), "alpha")
        self.assertEqual(selected_item(items, 2), "gamma")

    def test_index_past_the_end_returns_none(self) -> None:
        """An index equal to the length is out of range."""
        items = ["alpha", "beta"]
        self.assertIsNone(selected_item(items, 2))
        self.assertIsNone(selected_item(items, 100))

    def test_negative_index_returns_none(self) -> None:
        """Negative positions are out of range, not from the tail."""
        items = ["alpha", "beta"]
        self.assertIsNone(selected_item(items, -1))

    def test_empty_sequence_always_returns_none(self) -> None:
        """Any index on an empty sequence is out of range."""
        self.assertIsNone(selected_item([], 0))


if __name__ == "__main__":
    unittest.main()
