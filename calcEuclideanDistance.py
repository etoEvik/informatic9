import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import math

class DistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('calcEuclideanDistance')

        self.x1_input = QLineEdit()
        self.y1_input = QLineEdit()
        self.x2_input = QLineEdit()
        self.y2_input = QLineEdit()
        self.calculate_button = QPushButton('Calculate')
        self.result_label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.x1_input)
        layout.addWidget(self.y1_input)
        layout.addWidget(self.x2_input)
        layout.addWidget(self.y2_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.calculate_button.clicked.connect(self.calculateDistance)

        self.setLayout(layout)
        self.show()

    def calculateDistance(self):
        x1 = float(self.x1_input.text())
        y1 = float(self.y1_input.text())
        x2 = float(self.x2_input.text())
        y2 = float(self.y2_input.text())

        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.result_label.setText(str(distance))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = DistanceCalculator()
    sys.exit(app.exec_())
