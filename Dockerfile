FROM python:3.12.3-slim

RUN apt-get update && \
    apt-get -y install cron

ADD cronfile /etc/cron.d/cronfile
WORKDIR /app

COPY requirements.txt .
COPY utils/ ./utils/
COPY app.py .
COPY html_files/ ./html_files/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pandas-stubs

# Устанавливаем права на файл
RUN chmod 0644 /etc/cron.d/cronfile

# Устанавливаем новый крон-файл
RUN crontab /etc/cron.d/cronfile

EXPOSE 8501

# команда запуска приложения
CMD ["streamlit","run", "app.py"]