PYTHON=python3
ENV_DIR=.env_$(PYTHON)

define linebreak


endef

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
endif

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
	PYTHON_VERSION = $(shell . .env_python3/Scripts/activate && python pyver.py)
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
	PYTHON_VERSION = $(shell . .env_python3/bin/activate && python pyver.py)
endif

MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(MAKEFILE_PATH)))

PIP_WHL=dependencies/pip-22.0.3-py3-none-any.whl
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

.PHONY: test
test: build check-code mypy
	$(IN_ENV) tox

.PHONY: qt
qt:
	$(IN_ENV) python -m unittest discover --start-directory tests --verbose -b

.PHONY: artifacts
artifacts: build-reqs sdist wheel

$(ENV_DIR):
	virtualenv -p python3 $(ENV_DIR)

.PHONY: build-reqs
build-reqs: env
	$(IN_ENV) $(PIP_CMD) install build

.PHONY: build
build: env
	$(IN_ENV) $(PIP_CMD) install .[dev,docs]
	rm -rf $(ENV_DIR)/lib/$(PYTHON_VERSION)/site-packages/log_color
	ln -s $(MAKEFILE_DIR)/src/log_color $(MAKEFILE_DIR)/$(ENV_DIR)/lib/$(PYTHON_VERSION)/site-packages/

.PHONY: sdist
sdist: build-reqs
	$(IN_ENV) $(PYTHON) -m build --sdist

.PHONY: wheel
wheel: build-reqs
	$(IN_ENV) $(PYTHON) -m build --wheel

.PHONY: format-code
format-code:
	$(IN_ENV) black -l 119 src/ tests/ docs/source/conf.py

.PHONY: check-code
check-code:
	$(IN_ENV) black --check -l 119 src/ tests/ docs/source/conf.py

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
