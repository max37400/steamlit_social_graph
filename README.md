# Предисловие по steamlit_social_graph

В данном репозитории планируется прототип приложения стримлит по анализу данных и отрисовке графа, предварительно, на транзакционных данных.

Библиотеки:

-[pandas](https://pandas.pydata.org/)
-[pyvis](https://pyvis.readthedocs.io/en/latest/)
-[networkx](https://networkx.org/documentation/stable/index.html)

# Структура проекта

Предварительно взято из другого проекта, впоследствии будет заменено

```
steamlit_social_graph/
│
├── config/
│   ├─── openai_client.py
│   ├─── telegram_bot.py
│   └─── tokens.py
│
├── handlers/
│   ├── __init__.py
│   ├── command_handlers.py
│   └── message_handlers.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── app.py
├── Dockerfile
├── Makefile
└── requirements.txt
```

- `config/` - конфигурационные файлы
- `handlers/` - обработчики сообщений и команд
- `utils/` - вспомогательные функции
- `app.py` - главный файл приложения
- `Dockerfile` - скрипт для создания Docker образа
- `Makefile` - автоматизация процесса сборки
- `requirements.txt` - зависимости проекта