from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QFormLayout,
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

        slider_layout = QFormLayout()
        font_size_slider = QSlider(Qt.Orientation.Horizontal)
        font_color_slider = QSlider(Qt.Orientation.Horizontal)
        background_color_slider = QSlider(Qt.Orientation.Horizontal)

        slider_layout.addRow(QLabel("Font Size"), font_size_slider)
        slider_layout.addRow(QLabel("Background Color"), background_color_slider)
        slider_layout.addRow(QLabel("Font Size"), font_color_slider)

        root_layout.addLayout(slider_layout)
        self.setLayout(root_layout)


if __name__ == "__main__":
    app = QApplication([])

    win = StylizingWindow()
    win.show()

    app.exec()
