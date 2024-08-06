import os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        print(file)
        filepath = os.path.join(root, file)
        print(filepath)
        filetime = os.path.getmtime(filepath)
        print(filetime)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        print(filesize)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
