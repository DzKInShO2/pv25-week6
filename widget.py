from PyQt5.QtCore import (
    Qt,
    QMargins
)
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QWidget,
    QSlider,
    QLabel
)


class StylizingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 640, 360)
        self.setWindowTitle("Font Size and Color Adjuster")

        self.__setup_components()
        self.__setup_layout()

    def __setup_components(self):
        self.__font_size_slider = QSlider(Qt.Orientation.Horizontal)
        self.__font_size_slider.setTickPosition(
            QSlider.TickPosition.TicksBothSides)
        self.__font_size_slider.setTickInterval(5)
        self.__font_size_slider.setRange(0, 20)
        self.__font_size_slider.setSliderPosition(10)
        self.__font_size_slider.sliderMoved.connect(self.__change_font_size)

        self.__background_color_slider = QSlider(Qt.Orientation.Horizontal)
        self.__background_color_slider.setTickPosition(
            QSlider.TickPosition.TicksBothSides)
        self.__background_color_slider.setTickInterval(10)
        self.__background_color_slider.setRange(0, 255)
        self.__background_color_slider.setSliderPosition(255)
        self.__background_color_slider.sliderMoved.connect(
            self.__change_background_color)

        self.__font_color_slider = QSlider(Qt.Orientation.Horizontal)
        self.__font_color_slider.setTickPosition(
            QSlider.TickPosition.TicksBothSides)
        self.__font_color_slider.setTickInterval(10)
        self.__font_color_slider.setRange(0, 255)
        self.__font_color_slider.sliderMoved.connect(self.__change_font_color)

        self.__frame_box = QFrame()
        self.__frame_box.setStyleSheet("QFrame { background-color: #FFFFFF; }")

        self.__sid_label = QLabel("F1D02310110")
        self.__sid_label_size = 38
        self.__sid_label_color = "000000"
        self.__sid_label.setStyleSheet(f"""QFrame {{
            color: #{self.__sid_label_color};
            font-size: {self.__sid_label_size}pt;
        }}""")

    def __setup_layout(self):
        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(QMargins(32, 32, 32, 32))
        root_layout.setSpacing(12)

        frame_box_layout = QVBoxLayout()
        frame_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frame_box_layout.addWidget(self.__sid_label)
        self.__frame_box.setLayout(frame_box_layout)

        font_size_layout = QHBoxLayout()
        font_size_layout.addWidget(QLabel("Font Size"))
        font_size_layout.addWidget(self.__font_size_slider)

        background_color_layout = QHBoxLayout()
        background_color_layout.addWidget(QLabel("Background Color"))
        background_color_layout.addWidget(self.__background_color_slider)

        font_color_layout = QHBoxLayout()
        font_color_layout.addWidget(QLabel("Font Color"))
        font_color_layout.addWidget(self.__font_color_slider)

        root_layout.addWidget(QLabel("Dzakanov Inshoofi"), 0)
        root_layout.addWidget(self.__frame_box, 7)
        root_layout.addLayout(font_size_layout, 1)
        root_layout.addLayout(background_color_layout, 1)
        root_layout.addLayout(font_color_layout, 1)

        self.setLayout(root_layout)

    def __change_font_size(self, val):
        self.__sid_label_size = 38 + val
        self.__sid_label.setStyleSheet(f"""QFrame {{
            color: #{self.__sid_label_color};
            font-size: {self.__sid_label_size}pt;
        }}""")

    def __change_background_color(self, val):
        color = f"{val:02x}" * 3
        self.__frame_box.setStyleSheet(
            f"QFrame {{ background-color: #{color}; }}")

    def __change_font_color(self, val):
        self.__sid_label_color = f"{val:02x}" * 3
        self.__sid_label.setStyleSheet(f"""QFrame {{
            color: #{self.__sid_label_color};
            font-size: {self.__sid_label_size}pt;
        }}""")


if __name__ == "__main__":
    app = QApplication([])

    win = StylizingWindow()
    win.show()

    app.exec()
