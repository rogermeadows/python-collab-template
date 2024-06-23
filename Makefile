
VENV ?= env
BIN_DIR ?= $(VENV)/bin
HIDE ?= @
UTILS ?= utils

.PHONY: setup-venv setup clean-pyc clean-test test mypy lint docs check

setup-venv:
	$(HIDE)python3.12 -m venv $(VENV)
	$(HIDE)$(BIN_DIR)/pip3 install --upgrade pip
	$(HIDE)$(BIN_DIR)/pip3 install -r requirements.dev
	$(HIDE)$(BIN_DIR)/pip3 install -r requirements.prod

setup:
	 DOCKER_BUILDKIT=1 docker build -t dev -f Dockerfile .

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	find . -name '.pytest_cache' -exec rm -fr {} +

clean: clean-pyc clean-test
	find . -name '.my_cache' -exec rm -fr {} +
	rm -rf logs/

test-python: clean
	. $(VENV)/bin/activate && py.test tests --cov=src --cov-report=term-missing --cov-fail-under 95

test-pip:
	$(HIDE)$(BIN_DIR)/pip3 check --disable-pip-version-check
	$(HIDE)$(UTILS)/venv-pip-requirements-check.py $(BIN_DIR)/pip3

test-mypy:
	. $(VENV)/bin/activate && mypy src

test-lint:
	. $(VENV)/bin/activate && pylint src -j 4 --reports=y

test-flake8:
	. $(VENV)/bin/activate && flake8 src

docs: FORCE
	cd docs; . $(VENV)/bin/activate && sphinx-apidoc -o ./source ./src
	cd docs; . $(VENV)/bin/activate && sphinx-build -b html ./source ./build
FORCE:

checks: test-pip test-flake8 test-line test-mypy test-python clean

run-checks:
	docker run --rm -it --name run-checks -v $(shell pwd):/opt -t dev make checks

bash:
	docker run --rm -it --name run-checks -v $(shell pwd):/opt -t dev bash
