PYTHON=python3
ENV_DIR=.env_$(PYTHON)

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
endif


# Some distros need to use pip3 as the entrypoint
ifneq (, $(shell which pip3))
PIP_CMD=pip3
else ifneq (, $(shell which pip))
PIP_CMD=pip
else
$(error "Python's pip not found on $(PATH)")
endif

all: test format-code docs artifacts

env: $(ENV_DIR)

test: build check-code
	$(IN_ENV) tox

qt:
	$(IN_ENV) python -m unittest discover --start-directory tests --verbose -b

artifacts: build-reqs sdist wheel

$(ENV_DIR):
	virtualenv -p python3 $(ENV_DIR)

build-reqs: env
	$(IN_ENV) $(PIP_CMD) install sphinx black coverage wheel twine tox build setuptools_scm

build: build-reqs
	$(IN_ENV) $(PIP_CMD) install --editable .

sdist: build-reqs
	$(IN_ENV) $(PYTHON) -m build --no-isolation --sdist

wheel: build-reqs
	$(IN_ENV) $(PYTHON) -m build --no-isolation --wheel

format-code:
	$(IN_ENV) black -l 119 src/ tests/ setup.py docs/source/conf.py

check-code:
	$(IN_ENV) black --check -l 119 src/ tests/ setup.py docs/source/conf.py

docs: build-reqs
	$(IN_ENV) $(PIP_CMD) install -r docs/requirements.txt
	$(IN_ENV) $(MAKE) -C docs html

publish: artifacts
	$(IN_ENV) twine upload dist/*

# Static Analysis
mypy:
	$(IN_ENV) mypy --ignore-missing-imports src

freeze: env
	- $(IN_ENV) pip freeze

shell: env
	- $(IN_ENV) $(PYTHON)

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

env-clean: clean
	- @rm -rf .env*
	- @git clean -dfX
	- @rm -rf $(ENV_DIR)
	- @rm -rf .tox
