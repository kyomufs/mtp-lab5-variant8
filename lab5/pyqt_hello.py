"""Task 10 (medium): simplest GUI on PyQt5."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PyQt5.QtWidgets import QWidget


def build_window() -> QWidget:
    """Create a window with a label and a button.

    The button click handler replaces the label text with a fixed
    message. PyQt5 is imported inside the function, so the module is
    importable even when PyQt5 is not installed; the returned widget
    is not shown until the caller invokes ``show()``.

    Returns:
        The created widget window.
    """
    from PyQt5.QtWidgets import (
        QLabel,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )

    window = QWidget()
    label = QLabel("Hello from PyQt5!")
    button = QPushButton("Change the label")

    def handle_click() -> None:
        label.setText("The button was clicked")

    button.clicked.connect(handle_click)
    layout = QVBoxLayout(window)
    layout.addWidget(label)
    layout.addWidget(button)
    window.setWindowTitle("Lab 5 variant 8: PyQt5 hello")
    return window
