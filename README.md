# Предисловие по steamlit_social_graph

![Статусы тестов](https://github.com/max37400/steamlit_social_graph/actions/workflows/tests.yml/badge.svg)

В данном репозитории планируется прототип приложения стримлит по анализу данных и отрисовке графа, предварительно, на транзакционных данных.

Библиотеки:

-[streamlit](https://streamlit.io/)

-[pandas](https://pandas.pydata.org/)

-[pyvis](https://pyvis.readthedocs.io/en/latest/)

-[networkx](https://networkx.org/documentation/stable/index.html)

-[matplotlib](https://matplotlib.org/)

# Структура проекта

Предварительно взято из другого проекта, впоследствии будет заменено

```
steamlit_social_graph/
│
├── html_files/
│
├── utils/
│   ├── __init__.py
│   ├── data_deleter.py
|   └── data_loader.py
│
├── app.py
├── cronfile
├── Dockerfile
├── Makefile
└── requirements.txt
```

- `html_files/` - папка под генерируемые html-файлы
- `utils/` - "бэк" приложения
- `app.py` - главный файл приложения
- `cronfile` - задача для планировщика crontab
- `Dockerfile` - скрипт для создания Docker образа
- `Makefile` - автоматизация процесса сборки
- `requirements.txt` - зависимости проекта

---

# Часть 1: Локальная установка
## Установка проекта
0. Склонировать репозиторий
   ```
   git clone github.com/yourreponame
   ```
1. Установка зависимостей, генерация файла `.env`:
   ```
   make setup
   ```

## Запуск проекта

1. Запускаем приложение локально
   ```
   make run
   ```
# Часть 2: Разработка на облачном сервере

Для удаленной разработки потребуется:

- Доступ к Серверу (ssh user@ip & password)
- Visual Studio Code

#### Предустановленный софт на сервере:
- python3
- python3-venv
- docker-ce
- docker-ce-cli
- docker-buildx-plugin
- docker-compose-plugin

# Удаленная разработка
0. Заходим на сервер
  ```
  ssh -i PATH_TO_YOUR_KEY.pem username@SERVER_IP_ADDRESS
  ```

1. Клонируем (по https) свой репозиторий в отдельную папку на сервер
   ```
   git clone <repositorylink>
   ```
2. Установка зависимостей, генерация файла `.env`:
   ```
   make setup
   ```

---

# Запуск Docker контейнера

Для деплоя контейнера на облачный сервер потребуется:

- Скаченная программа [Docker](https://www.docker.com/products/docker-desktop/)
- Аккаунт в [DockerHub](https://hub.docker.com/)
- [Создать репозиторий](https://docs.docker.com/docker-hub/repos/create/)
- операционная система Linux или MacOS

1. В `Makefile` добавим **username** и **repositoryname**:

   ```
   # данные пользователя на Docker Hub
   USERNAME=UserNameDockerHub
   REPO=RepositoryNameDockerHub
   TAG=v1
   ```
#### Для публикации образа в [DockerHub](https://hub.docker.com/) нужно залогиниться через CLI командой `docker login`


2. Собираем образ:

   ```
   make build
   ```

3. Запускаем контейнер с приложением

  ```
   make dockerrun
  ```

4. Также, можно опубликовать образ в DockerHub:

   ```
   make push
   ```

---

## Скачивание и запуск опубликованного образа

1. Находим опубликованный образ в DockerHub:

   ```
   docker search username/projectname
   ```

2. Скачиваем образ:

   ```
   docker pull username/projectname:v1
   ```

3. Запускаем контейнер с токенами Telegram бота и OpenAI API:

   ```
   sudo docker run -p 8501:8501 username/projectname:v1
   ```

4. Открываем страницу в вебе и пользуемся