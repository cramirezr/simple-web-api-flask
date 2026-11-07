install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-ruff-alt:
	pip install --upgrade pip &&\
		pip install -r requirements-lint-alt.txt

format:
	black *.py

format-ruff:
	ruff format *.py

ruff-format-lint:
	ruff check --fix . &&\
		ruff format .

lint-pylint:
	pylint --disable=R,C app.py

test:
	python -m pytest -vv --cov=app test_app.py

all: install format lint-pylint test
all-ruff: install-ruff-alt ruff-format-lint test