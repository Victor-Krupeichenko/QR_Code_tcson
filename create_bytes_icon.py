import base64

# 1. Открываю файл картинки в режиме чтения байт ("rb")
with open("tcson.png", "rb") as image_file:
    # 2. Кодирую байты в формат Base64
    base64_bytes = base64.b64encode(image_file.read())

    # 3. Декодирую байты в обычную текстовую строку (string)
    base64_text = base64_bytes.decode("utf-8")

# 4. Записываю получившуюся длинную строку в текстовый файл
with open("encoded_image.txt", "w") as text_file:
    text_file.write(base64_text)

print("Картинка успешно сконвертирована! Результат сохранен в файл encoded_image.txt")
