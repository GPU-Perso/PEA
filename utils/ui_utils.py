from PySide2.QtWidgets import (
    QLabel
)
from PySide2.QtCore import Qt

def create_label(text: str, width: int = None, alignment: Qt.Alignment = None, format: str = None):
    if text and format:
        s = "{t"+format+"}"
        l = QLabel(s.format(t=float(text)))
    else:
        l = QLabel(text)
    if width:
        l.setFixedWidth(width)
    if alignment:
        l.setAlignment(alignment)

    return l

def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clear_layout(child.layout())

def colorize_label(label: QLabel, color, value=None, min=None, max=None):
    if not value or not min and not max:
        return
    if min and value < min or max and value > max:
        label.setStyleSheet(f"color: {color};")
    else:
        label.setStyleSheet(f"color: black;")