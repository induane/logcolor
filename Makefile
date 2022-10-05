# Select Python 3.8, 3.9 or 3.10 (or error out)
ifneq (, $(shell command -v python3.8))
PYTHON=python3.8
else ifneq (, $(shell command -v python3.9))
PYTHON=python3.9
else ifneq (, $(shell command -v python3.10))
PYTHON=python3.10
else ifneq (, $(shell command -v python3.11))
PYTHON=python3.11
else
$(error "No Python version 3.6, 3.7, 3.8, 3.9 or 3.10 found on: $(PATH)")
endif

ENV_DIR=.env_$(PYTHON)

define linebreak


endef

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
endif

MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(MAKEFILE_PATH)))

PIP_WHL=dependencies/pip-22.2.2-py3-none-any.whl
PIP_CMD=$(PYTHON) $(PIP_WHL)/pip

ifeq (, $(shell command -v pyre))
$(warning "pyre not found on $(PATH).")
endif

# Make sure virtualenv is present
ifeq (, $(shell command -v virtualenv))
$(error "virtualenv command not found in $(PATH)")
endif

.PHONY: all
all: test format-code docs artifacts

env: $(ENV_DIR)

.PHONY: qt
qt:
	$(IN_ENV) python -m unittest discover --start-directory tests --verbose -b

.PHONY: test
test: build check-code mypy qt

.PHONY: artifacts
artifacts: build-reqs sdist wheel

$(ENV_DIR):
	virtualenv -p $(PYTHON) $(ENV_DIR)

.PHONY: build-reqs
build-reqs: env
	$(IN_ENV) $(PIP_CMD) install build

.PHONY: build
build: env
	$(IN_ENV) $(PIP_CMD) install -e .[dev,docs]

.PHONY: sdist
sdist: build-reqs
	$(IN_ENV) $(PYTHON) -m build --sdist

.PHONY: wheel
wheel: build-reqs
	$(IN_ENV) $(PYTHON) -m build --wheel

.PHONY: format-code
format-code:
	$(IN_ENV) black src/ tests/ docs/source/conf.py
	$(IN_ENV) isort src/ tests/ docs/source/conf.py

.PHONY: check-code
check-code:
	$(IN_ENV) black --check src/ tests/ docs/source/conf.py
	$(IN_ENV) isort --check-only src/ tests/ docs/source/conf.py

.PHONY: docs
docs: build-reqs
	$(IN_ENV) $(MAKE) -C docs html

.PHONY: publish
publish: artifacts
	$(IN_ENV) twine upload dist/*

# Static Analysis

.PHONY: mypy
mypy:
	$(IN_ENV) mypy src/

.pyre_configuration:
	$(error "$(linebreak)========================================$(linebreak)Missing PYRE configuration file!$(linebreak)========================================$(linebreak)You must initialize a pyre environment$(linebreak)Command:  pyre init$(linebreak)Select :  'n' for watchman$(linebreak)Select :  'src' for analysis directory$(linebreak)========================================$(linebreak)")

.PHONY: pyre
pyre: .pyre_configuration
	$(IN_ENV) pyre

.PHONY: freeze
freeze: env
	- $(IN_ENV) pip freeze

.PHONY: shell
shell: env
	- $(IN_ENV) $(PYTHON)

.PHONY: clean
clean:
	- @rm -rf BUILD
	- @rm -rf BUILDROOT
	- @rm -rf RPMS
	- @rm -rf SRPMS
	- @rm -rf SOURCES
	- @rm -rf docs/build
	- @rm -rf src/*.egg-info
	- @rm -rf build
	- @rm -rf dist
	- @rm -f .coverage
	- @rm -f test_results.xml
	- @rm -f coverage.xml
	- @rm -f tests/coverage.xml
	- @rm -f pep8.out
	- @find . -name '*.orig' -delete
	- @find . -name '*.DS_Store' -delete
	- @find . -name '*.pyc' -delete
	- @find . -name '*.pyd' -delete
	- @find . -name '*.pyo' -delete
	- @find . -name '*__pycache__*' -delete

.PHONY: env-clean
env-clean: clean
	- @rm -rf .env*
	- @git clean -dfX
	- @rm -rf $(ENV_DIR)
	- @rm -rf .tox
