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

        self.setGeometry(0, 0, 640, 480)
        self.setWindowTitle("The Window")

        self.__setup_components()
        self.__setup_layout()

    def __setup_components(self):
        self.__font_size_slider = QSlider(Qt.Orientation.Horizontal)
        self.__font_size_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.__font_size_slider.setTickInterval(5)
        self.__font_size_slider.setRange(0, 20)

        self.__background_color_slider = QSlider(Qt.Orientation.Horizontal)
        self.__background_color_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.__background_color_slider.setTickInterval(10)
        self.__background_color_slider.setRange(0, 255)

        self.__font_color_slider = QSlider(Qt.Orientation.Horizontal)
        self.__font_color_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.__font_color_slider.setTickInterval(10)
        self.__font_color_slider.setRange(0, 255)

    def __setup_layout(self):
        root_layout = QVBoxLayout()

        font_size_layout = QHBoxLayout()
        font_size_layout.addWidget(QLabel("Font Size"))
        font_size_layout.addWidget(self.__font_size_slider)

        background_color_layout = QHBoxLayout()
        background_color_layout.addWidget(QLabel("Background Color"))
        background_color_layout.addWidget(self.__background_color_slider)

        font_color_layout = QHBoxLayout()
        font_color_layout.addWidget(QLabel("Font Color"))
        font_color_layout.addWidget(self.__font_color_slider)

        root_layout.addLayout(font_size_layout)
        root_layout.addLayout(background_color_layout)
        root_layout.addLayout(font_color_layout)

        self.setLayout(root_layout)


if __name__ == "__main__":
    app = QApplication([])

    win = StylizingWindow()
    win.show()

    app.exec()
