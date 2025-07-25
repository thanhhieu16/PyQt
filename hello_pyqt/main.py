import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.greet)

    def greet(self):
        name = self.ui.lineEdit.text()
        self.ui.label.setText(f"Xin chào, {name}!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
