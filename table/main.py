import sys
import os
from PyQt5 import QtWidgets
from table import Ui_TableForm

class TableApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Bảng danh sách sinh viên")

        # Gắn sự kiện
        self.ui.btn_add.clicked.connect(self.add_row)
        self.ui.btn_delete.clicked.connect(self.delete_selected_rows)

        # Thiết lập bảng
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Họ tên", "Email", "Điện thoại"])

    def add_row(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

    def delete_selected_rows(self):
        selected = self.ui.tableWidget.selectionModel().selectedRows()
        for row in sorted(selected, reverse=True):
            self.ui.tableWidget.removeRow(row.row())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TableApp()

    # Load style nếu có
    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r") as f:
            app.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec_())
