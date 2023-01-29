APP_DIR ?= $(shell pwd)
PYTHON ?= 3.8
PYTESTARGS ?=
POETRY_VENV = .poetry_venv
POETRY ?= ${POETRY_VENV}/bin/poetry

${POETRY_VENV}:
	python -m venv ${POETRY_VENV}
	${POETRY_VENV}/bin/pip install pip -U
	${POETRY_VENV}/bin/pip install poetry 
	${POETRY} config virtualenvs.in-project true
	${POETRY} config virtualenvs.create true

.LOW_RESOLUTION_TIME: poetry.lock pyproject.toml
poetry.lock: pyproject.toml | ${POETRY_VENV}
	${POETRY} lock
	touch poetry.lock

.venv: poetry.lock | ${POETRY_VENV}
	${POETRY} install --remove-untracked

env: | .venv
	ln -s .venv env

.PHONY: develop
develop: env

.PHONY: install
install: develop

.PHONY: clean
clean:
	rm -rf ${POETRY_VENV} env .venv .cache *.egg-info dist build coverage.xml unittest_results.xml .coverage
	find . -type f -name \*.pyc -delete

.PHONY: mypy
mypy: develop
	${POETRY} run mypy

.PHONY: test
test: develop
	${POETRY} run pytest

.PHONY: wheel
wheel: ${POETRY_VENV}
	${POETRY} build

