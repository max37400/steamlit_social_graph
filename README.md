# Предисловие по steamlit_social_graph

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
│   ├── data_loader.py
|   └── data_deleter.py
│
├── app.py
├── Dockerfile (to be done)
├── Makefile (to be done)
└── requirements.txt
```

- `config/` - конфигурационные файлы
- `handlers/` - обработчики сообщений и команд
- `utils/` - вспомогательные функции
- `app.py` - главный файл приложения
- `Dockerfile` - скрипт для создания Docker образа
- `Makefile` - автоматизация процесса сборки
- `requirements.txt` - зависимости проекта