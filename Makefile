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
	$(PYTHON_VENV) app.py