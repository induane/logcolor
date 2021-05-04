ENV_DIR=.env

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate &&
endif

all: test format-code docs artifacts

env: $(ENV_DIR)

test: build check-code
	$(IN_ENV) tox

artifacts: build-reqs sdist wheel

$(ENV_DIR):
	virtualenv -p python3 $(ENV_DIR)

build-reqs: env
	$(IN_ENV) pip install sphinx black coverage wheel twine tox

build: build-reqs
	$(IN_ENV) pip install --editable .

sdist: build-reqs
	$(IN_ENV) python setup.py sdist

wheel: build-reqs
	$(IN_ENV) python setup.py bdist_wheel

format-code:
	$(IN_ENV) black -l 119 src/ tests/ setup.py

check-code:
	$(IN_ENV) black --check -l 119 src/ tests/ setup.py

docs: build-reqs
	$(IN_ENV) pip install -r docs/requirements.txt
	$(IN_ENV) $(MAKE) -C docs html

publish: artifacts
	$(IN_ENV) twine upload dist/*

freeze: env
	- $(IN_ENV) pip freeze

shell: env
	- $(IN_ENV) python

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
