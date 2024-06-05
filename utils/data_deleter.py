import os
import datetime

# Путь к папке, в которой нужно удалять старые файлы
folder_path = "/home/max37400/steamlit_social_graph/html_files"

# Время, после которого файлы будут удалены (в данном случае 2 часа)
threshold = datetime.datetime.now() - datetime.timedelta(hours=2)

# Проход по всем файлам в папке
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # Получение времени последнего изменения файла
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    
    # Удаление файла, если он старше порогового времени
    if modified_time < threshold and file_path.endswith('html'):
        os.remove(file_path)
print('Script was here!')