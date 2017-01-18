ENV_DIR=.env

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
endif

all: test lint docs artifacts

env: $(ENV_DIR)

test: build
	$(IN_ENV) tox

artifacts: build_reqs sdist wheel

$(ENV_DIR):
	virtualenv -p python $(ENV_DIR)

build_reqs: env
	$(IN_ENV) pip install sphinx pep8 coverage nose wheel twine tox

build: build_reqs
	$(IN_ENV) pip install --editable .

sdist: build_reqs
	$(IN_ENV) python setup.py sdist

wheel: build_reqs
	$(IN_ENV) python setup.py bdist_wheel

lint: pep8

pep8: build_reqs
	- $(IN_ENV) pep8 src/logcolor > pep8.out

docs: build_reqs
	$(IN_ENV) pip install -r docs/requirements.txt
	$(IN_ENV) $(MAKE) -C docs html

publish: artifacts
	$(IN_ENV) twine upload dist/*

freeze: env
	- $(IN_ENV) pip freeze

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
	- find -name '*.pyc' -delete
	- find -name '*.pyo' -delete
	- find -name '*.pyd' -delete
	- find -name '*__pycache__*' -delete

env_clean: clean
	- @rm -rf .env*
	- @rm -rf $(ENV_DIR)
	- @rm -rf .tox
