import sys
import os
import resources_rc
from PyQt5 import QtWidgets, QtGui, QtCore
from viewer import Ui_ImageViewer

class ImageViewer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ImageViewer()
        self.ui.setupUi(self)

        self.setWindowTitle("Trình xem ảnh nâng cao")

        # Load QSS
        qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r") as f:
                self.setStyleSheet(f.read())

        self.ui.btn_open.clicked.connect(self.open_image)
        self.ui.btn_zoom_in.clicked.connect(self.zoom_in)
        self.ui.btn_zoom_out.clicked.connect(self.zoom_out)
        self.ui.btn_rotate_left.clicked.connect(self.rotate_left)
        self.ui.btn_rotate_right.clicked.connect(self.rotate_right)

        # Zoom state
        self.scale_factor = 1.0
        self.rotation = 0

        # Lắng nghe sự kiện lăn chuột trên label
        self.ui.label_image.installEventFilter(self)

        # Cho phép kéo-thả file vào cửa sổ
        self.setAcceptDrops(True)

    def open_image(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path):
        if os.path.exists(file_path):
            self.original_pixmap = QtGui.QPixmap(file_path)
            self.scale_factor = 1.0
            self.rotation = 0
            self.update_image_display()

    def update_image_display(self):
        if hasattr(self, "original_pixmap"):
            pixmap = self.original_pixmap

            # Xoay
            transform = QtGui.QTransform().rotate(self.rotation)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)

            # Zoom
            scaled = pixmap.scaled(
                pixmap.size() * self.scale_factor,
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )

            self.ui.label_image.setPixmap(scaled)

    def zoom_in(self):
        self.scale_factor *= 1.1
        self.update_image_display()

    def zoom_out(self):
        self.scale_factor /= 1.1
        self.update_image_display()

    def rotate_left(self):
        self.rotation -= 90
        self.update_image_display()

    def rotate_right(self):
        self.rotation += 90
        self.update_image_display()

    def eventFilter(self, source, event):
        if source == self.ui.label_image and event.type() == QtCore.QEvent.Wheel:
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()
            return True
        return super().eventFilter(source, event)

    # Kéo - Thả ảnh
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.toLocalFile().lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                self.load_image(file_path)
                break

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
