import sys
from PySide6.QtWidgets import QApplication, QDialog
from QR_tcson import Ui_Dialog
from qrcode_generate import QrcodeGenerate


class QRCodeGenerator(QDialog):
    """
    Класс для запуска приложения
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.run)

    def run(self):
        """
        Запускает генерацию QR-кода
        """
        user_text = self.ui.textEdit.toPlainText()
        if user_text:
            qrcode_generator = QrcodeGenerate(user_text)
            qrcode_generator.main()
            self.ui.textEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeGenerator()
    window.show()
    sys.exit(app.exec())
