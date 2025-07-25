import sys
import os
from PyQt5 import QtWidgets
from form import Ui_RegisterForm

class RegisterWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterForm()
        self.ui.setupUi(self)
        
        qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
        with open(qss_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)
            
        # Gọi self.center() sau setupUi
        self.center()
        # Kết nối nút Đăng ký
        self.ui.btn_register.clicked.connect(self.handle_register)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def handle_register(self):
        name = self.ui.lineEdit_name.text()
        email = self.ui.lineEdit_email.text()
        password = self.ui.lineEdit_password.text()
        confirm = self.ui.lineEdit_confirm.text()

        if not name or not email or not password or not confirm:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
        elif password != confirm:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Mật khẩu không khớp.")
        else:
            QtWidgets.QMessageBox.information(self, "Thành công", f"Chào {name}, bạn đã đăng ký thành công!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
