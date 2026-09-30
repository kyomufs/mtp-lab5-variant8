"""Tests for the notes program (advanced no.1)."""

import json
import tempfile
import unittest
from pathlib import Path

import lab5.notes_app
from lab5.notes import NotesModel


class NotesModelTests(unittest.TestCase):
    """Checks for :class:`lab5.notes.NotesModel`."""

    def test_add_collects_notes_in_order(self) -> None:
        """Notes are appended and returned in insertion order."""
        model = NotesModel()
        model.add("buy milk")
        model.add("write lab 5")
        self.assertEqual(model.all(), ["buy milk", "write lab 5"])

    def test_all_returns_a_copy(self) -> None:
        """Mutating the returned list does not touch the model."""
        model = NotesModel(["seed"])
        snapshot = model.all()
        snapshot.append("mutated")
        self.assertEqual(model.all(), ["seed"])

    def test_save_and_load_roundtrip(self) -> None:
        """A saved model is restored with the same notes."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.json"
            source = NotesModel()
            source.add("first note")
            source.add("second note")
            source.save(path)

            raw = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(raw, ["first note", "second note"])

            expected = ["first note", "second note"]
            restored = NotesModel(["stale note"])
            restored.load(path)
            self.assertEqual(restored.all(), expected)

    def test_save_keeps_unicode_readable(self) -> None:
        """Non-ASCII text is stored literally, not as escapes."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.json"
            model = NotesModel()
            model.add("привет")
            model.save(path)
            content = path.read_text(encoding="utf-8")
            self.assertIn("привет", content)

    def test_load_missing_file_raises(self) -> None:
        """Loading a nonexistent file reports FileNotFoundError."""
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "absent.json"
            with self.assertRaises(FileNotFoundError):
                NotesModel().load(missing)

    def test_load_rejects_non_array_payload(self) -> None:
        """A JSON object instead of an array is rejected."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text('{"notes": []}', encoding="utf-8")
            with self.assertRaises(ValueError):
                NotesModel().load(path)

    def test_load_rejects_non_string_items(self) -> None:
        """An array holding non-string values is rejected."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text("[1, 2]", encoding="utf-8")
            with self.assertRaises(ValueError):
                NotesModel().load(path)

    def test_notes_app_imports_without_display(self) -> None:
        """The Tkinter wrapper module loads headless."""
        self.assertTrue(
            callable(lab5.notes_app.build_notes_window)
        )


if __name__ == "__main__":
    unittest.main()
