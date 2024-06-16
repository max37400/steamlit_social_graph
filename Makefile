USERNAME=UserNameDockerHub
REPO=RepositoryNameDockerHub
TAG=v1

IMAGE = $(USERNAME)/$(REPO):$(TAG)

PYTHON=python3
PIP=.venv/bin/pip
PYTHON_VENV=.venv/bin/python

# создание виртуального окружения
setup:
	@echo "Setup venv, install requirements and create .env"
	$(PYTHON) -m venv .venv
	$(PIP) install -r requirements.txt

# запуск приложения
run:
	@echo "Run app"
	$(PYTHON_VENV) -m streamlit run app.py

# запуск приложения в Docker
dockerrun:
	@echo "Docker run"
	sudo docker run -d -p 8501:8501 $(IMAGE)

# сборка образа
build:
	@echo "Build image for $(IMAGE)"
	sudo docker build --platform linux/amd64 -t $(IMAGE) .

# публикация образа
push:
	@echo "Push image to $(IMAGE)"
	sudo docker push $(IMAGE)
