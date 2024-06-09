"""Модуль для периодического удаления старых файлов"""
import os
import datetime

# Путь к папке, в которой нужно удалять старые файлы
FOLDER_PATH = "/home/max37400/steamlit_social_graph/html_files"

# Время, после которого файлы будут удалены (в данном случае 2 часа)
threshold = datetime.datetime.now() - datetime.timedelta(hours=2)

# Проход по всем файлам в папке
for file_name in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file_name)
    # Получение времени последнего изменения файла
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    # Удаление файла, если он старше порогового времени
    if modified_time < threshold and file_path.endswith('html'):
        os.remove(file_path)
print('Script was here!')
