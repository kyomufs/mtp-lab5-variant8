"""Advanced task 1: notes storage with JSON persistence."""

from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path


class NotesModel:
    """In-memory list of notes that can be stored as JSON."""

    def __init__(self, notes: Sequence[str] = ()) -> None:
        """Create a model pre-filled with a copy of ``notes``."""
        self._notes: list[str] = list(notes)

    def add(self, text: str) -> None:
        """Append ``text`` to the end of the note list."""
        self._notes.append(text)

    def all(self) -> list[str]:
        """Return a copy of all notes in insertion order."""
        return list(self._notes)

    def save(self, path: str | Path) -> None:
        """Write all notes to ``path`` as a JSON array of strings.

        An existing file is overwritten; non-ASCII characters are
        stored as-is instead of ``\\uXXXX`` escapes.
        """
        target = Path(path)
        payload = json.dumps(self._notes, ensure_ascii=False, indent=2)
        target.write_text(payload, encoding="utf-8")

    def load(self, path: str | Path) -> None:
        """Replace current notes with the JSON array stored at ``path``.

        Raises:
            FileNotFoundError: if ``path`` does not exist.
            ValueError: if the file does not contain a JSON array of
                strings.
        """
        target = Path(path)
        data = json.loads(target.read_text(encoding="utf-8"))
        valid = isinstance(data, list) and all(
            isinstance(item, str) for item in data
        )
        if not valid:
            raise ValueError(
                "notes file must contain a JSON array of strings"
            )
        self._notes = list(data)
