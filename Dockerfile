FROM python:3.12.3-slim
WORKDIR /app

COPY requirements.txt .
COPY utils/ ./utils/
COPY app.py .
COPY html_files/ ./html_files/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

# команда запуска приложения
CMD ["streamlit","run", "app.py"]