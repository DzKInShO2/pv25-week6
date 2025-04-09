from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QSlider,
    QLabel
)


class StylizingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(640, 640)
        self.setWindowTitle("The Window")

        self.__create_components()

    def __create_components(self):
        root_layout = QVBoxLayout()

        self.setLayout(root_layout)


if __name__ == "__main__":
    app = QApplication([])

    win = StylizingWindow()
    win.show()

    app.exec()
