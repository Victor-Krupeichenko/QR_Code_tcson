import qrcode
import os
import base64
import io
from datetime import datetime
from PIL import Image, ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PySide6.QtCore import QCoreApplication
from logo_icon import logo_icon_bytes


class QrcodeGenerate:
    """
    Класс для генерации QR-кода
    """

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
        # applicationDirPath() возвращает чистый путь к папке,
        # где физически лежит запущенный пользователем файл .exe
        self.base_dir = QCoreApplication.applicationDirPath()

        # Декодирую встроенный логотип из памяти
        self.logo_data_bytes = base64.b64decode(logo_icon_bytes)

    def add_data(self):
        """
        Добавляет данные и генерирует матрицу
        """
        bytes_data = self.data.encode('utf-8')
        self.qr.add_data(bytes_data)
        self.qr.make(fit=True)

    def _prepare_logo(self, qr_width):
        """
        Читает картинку НАПРЯМУЮ ИЗ ПАМЯТИ, обрезает в круг и делает белую рамку
        """
        try:
            # читаю из байтов: io.BytesIO делает виртуальный файл прямо в ОЗУ
            logo = Image.open(io.BytesIO(self.logo_data_bytes)).convert("RGBA")

            # Вычисляю размер: здание будет занимать 35% от ширины QR-кода
            logo_size = int(qr_width * 0.35)
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

            # Делаю картинку здания круглой с помощью маски
            mask = Image.new("L", (logo_size, logo_size), 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse((0, 0, logo_size, logo_size), fill=255)

            round_logo = Image.new("RGBA", (logo_size, logo_size))
            round_logo.paste(logo, (0, 0), mask=mask)

            # Создаю белую круглую подложку-рамку
            padding = 5  # Толщина белого отступа вокруг здания
            bg_size = logo_size + (padding * 2)

            logo_bg = Image.new("RGBA", (bg_size, bg_size), (0, 0, 0, 0))
            draw_bg = ImageDraw.Draw(logo_bg)
            draw_bg.ellipse((0, 0, bg_size, bg_size), fill="white")

            # Накладываю круглое здание на белую подложку
            logo_bg.paste(round_logo, (padding, padding), mask=round_logo)
            return logo_bg

        except Exception as e:
            print(f"Ошибка загрузки встроенного логотипа: {e}")
            return None

    def changes_block(self):
        """
        Изменяет блок, красит код в синий цвет и накладывает картинку здания в центр
        """
        # Сначала генерирую базовый закругленный QR-код с цветовой маской
        self.img = self.qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(radius_ratio=0.4),  # Оптимально для сканирования телефоном!
            eye_drawer=RoundedModuleDrawer(radius_ratio=1.0),  # закругляю углы квадратов по краям
            color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(0, 0, 255))
        ).convert("RGB")

        # Получаю подготовленную круглую картинку здания с рамкой
        qr_width, _ = self.img.size
        logo_bg = self._prepare_logo(qr_width)

        # Если картинка успешно обработана, центрирую и накладываю её на QR-код
        if logo_bg:
            bg_size = logo_bg.size[0]
            center_pos = ((qr_width - bg_size) // 2, (qr_width - bg_size) // 2)
            self.img.paste(logo_bg, center_pos, mask=logo_bg)

    def save_image(self):
        """
        Сохраняет картинку в папку 'QR-Code' строго рядом с файлом запуска .exe
        """
        target_folder = os.path.join(self.base_dir, "QR-Code")

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")

        file_name = f"QR-code-Loev-tcson({timestamp}).png"
        full_path = os.path.join(target_folder, file_name)

        self.img.save(full_path)
        print(f"Успешно сохранено по настоящему пути: {full_path}")

    def main(self):
        """
        Основной метод(запускает генерацию QR-кода)
        """
        self.add_data()
        self.changes_block()
        self.save_image()
