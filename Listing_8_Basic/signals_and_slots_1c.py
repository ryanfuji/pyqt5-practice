import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.button_is_checked = True
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)

        # Set the central widget of the Window
        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
