import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer


class QrcodeGenerate:

    def __init__(self, data):
        """
        :param data: Данные которые нужно записать в QR-код
        """
        self.data = data
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        self.img = None

    def add_data(self):
        """
        Добавляет данные и генерирует матрицу
        """
        self.qr.add_data(self.data)
        self.qr.make(fit=True)

    def changes_block(self):
        """
        Изменяет блок
        """
        self.img = self.qr.make_image(
            image_factory=StyledPilImage,
            eye_drawer=RoundedModuleDrawer(radius_ratio=1.0),
            fill_color="black",
            back_color="while"
        )

    def save_image(self):
        """
        Сохраняет картинку
        """
        self.img.save("QR-code-Loev-tcson.png")

    def main(self):
        """
        Основной метод(запускает генерацию QR-кода)
        """
        self.add_data()
        self.changes_block()
        self.save_image()
