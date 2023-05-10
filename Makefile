
.PHONY: Makefile

.PHONY: test
test:
	python3 -m pytest -vv -s --ignore=tests/api_tests

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
	coverage run --source='.' -m pytest -vv --disable-pytest-warnings -o log_cli=true -s --ignore=tests/api_tests;
	coverage report;
	coverage-badge -o coverage.svg;

.PHONY: venv-init deps freeze_dev freeze_prod clean_venv
all: venv-init deps
	PYTHONPATH=.venv ; source .venv/bin/activate
venv-init:
	if [ ! -e ".venv/bin/activate" ] ; then PYTHONPATH=.venv ; python3 -m venv .venv ; fi
deps:
	 . .venv/bin/activate && pip install --upgrade pip fi
	 . .venv/bin/activate && pre-commit install
freeze_dev:
	. .venv/bin/activate && poetry export -f requirements.txt --output requirements-dev.txt \
	--with=dev \
	--without-hashes \
	--without-urls
freeze_prod:
	. .venv/bin/activate && poetry export -f requirements.txt --output requirements.txt \
	--only=main \
	--without-hashes \
	--without-urls
.PHONY: freeze
freeze: freeze_prod
rm-env:
	rm -rf .venv
venv-recreate: rm-env venv-init deps
env:
	. .venv/bin/activate.fish
