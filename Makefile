SHELL := /bin/bash

venv:
	python3 -m venv .venv

activate:
	@echo "(the next line will be copied into your clipboard, simply paste it)"
	@echo "source .venv/bin/activate"
	@echo "source .venv/bin/activate" | pbcopy

install: requirements.txt
	pip install -r requirements.txt

run:
	python app.py

freeze:
	pip freeze > requirements.txt

clean:
	rm -rf src/__pycache__

pipupgrade:
	pip install --upgrade pip
