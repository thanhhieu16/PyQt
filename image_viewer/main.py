import sys
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from viewer import Ui_ImageViewer

class ImageViewer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ImageViewer()
        self.ui.setupUi(self)

        self.setWindowTitle("Trình xem ảnh")

        # Load style QSS nếu có
        qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r") as f:
                self.setStyleSheet(f.read())

        self.ui.btn_open.clicked.connect(self.open_image)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            pixmap = QtGui.QPixmap(file_path)
            self.ui.label_image.setPixmap(pixmap.scaled(
                self.ui.label_image.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
