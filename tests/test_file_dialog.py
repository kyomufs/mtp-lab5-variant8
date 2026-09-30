"""Tests for the file dialog task (medium no.8)."""

import unittest

import lab5.file_dialog
from lab5.file_dialog import choose_file


class ChooseFileTests(unittest.TestCase):
    """Checks for :func:`lab5.file_dialog.choose_file`."""

    def test_module_imports_without_tkinter(self) -> None:
        """The module imports headless and exposes its builder."""
        self.assertTrue(callable(lab5.file_dialog.build_file_window))

    def test_returns_path_from_injected_dialog(self) -> None:
        """A path returned by the dialog is passed through."""
        calls: list[str] = []

        def fake_dialog() -> str:
            calls.append("called")
            return "/home/user/report.txt"

        self.assertEqual(
            choose_file(fake_dialog), "/home/user/report.txt"
        )
        self.assertEqual(len(calls), 1)

    def test_empty_string_means_cancellation(self) -> None:
        """An empty dialog result is normalised to ``None``."""
        self.assertIsNone(choose_file(lambda: ""))


if __name__ == "__main__":
    unittest.main()
