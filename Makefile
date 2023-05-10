
.PHONY: Makefile

.PHONY: test
test:
	python3 -m pytest -vv -s

.PHONY: cyclo
cyclo:
	radon cc mapping -s

.PHONY: format
format:
	black .
	autoflake --recursive --in-place --exclude .venv .
	isort --atomic --skip .venv .

format-check:
	. .venv/bin/activate && flake8 --config=./setup.cfg ./

.PHONY: coverage
coverage:
	rm -f coverage.svg;
	coverage erase;
	coverage run --source='.' -m pytest -vv --disable-pytest-warnings -o log_cli=true -s;
	coverage report;
	coverage-badge -o coverage.svg;

.PHONY: venv-init deps freeze_dev freeze_prod clean_venv
all: venv-init deps
	PYTHONPATH=.venv ; source .venv/bin/activate
venv-init:
	if [ ! -e ".venv/bin/activate" ] ; then PYTHONPATH=.venv ; python3 -m venv .venv ; fi
deps:
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -r requirements.txt
	. .venv/bin/activate && pre-commit install

.PHONY: freeze
freeze:
	pip freeze > requirements.txt
rm-venv:
	rm -rf .venv
venv-recreate: rm-venv venv-init deps
env:
	( \
       source .venv/bin/activate; \
    )
