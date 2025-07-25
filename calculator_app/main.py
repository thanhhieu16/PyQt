from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import os
from ui_calculator import Ui_Calculator

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        
        # 👉 Load QSS từ file
        qss_path = os.path.join(os.path.dirname(__file__), "dark.qss")
        with open(qss_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
            
        # Tăng cỡ chữ cho lineEdit
        font = QFont()
        font.setPointSize(24)  # Bạn có thể điều chỉnh số này cho phù hợp
        self.ui.lineEdit.setFont(font)
        
        # Không cho phép nhập vào lineEdit
        self.ui.lineEdit.setReadOnly(True)
        
        self.ui.lineEdit.setAlignment(Qt.AlignRight)

        # Kết nối sự kiện các nút
        self.connectSignals()

    def connectSignals(self):
        # Số và dấu chấm
        for btn in ['btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                    'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9', 'btn_dot']:
            getattr(self.ui, btn).clicked.connect(
                lambda _, b=btn: self.appendToLine(getattr(self.ui, b).text())
            )

        # Các phép tính
        for op in ['btn_plus', 'btn_minus', 'btn_multiply', 'btn_divide']:
            getattr(self.ui, op).clicked.connect(
                lambda _, b=op: self.appendToLine(getattr(self.ui, b).text())
            )

        # Nút =
        self.ui.btn_equal.clicked.connect(self.calculate)
        
        # Nút C (clear)
        self.ui.btn_clear.clicked.connect(lambda: self.ui.lineEdit.clear())

    def appendToLine(self, text):
        current = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(current + text)

    def calculate(self):
        try:
            result = str(eval(self.ui.lineEdit.text()))
            self.ui.lineEdit.setText(result)
        except:
            self.ui.lineEdit.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
