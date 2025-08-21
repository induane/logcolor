# A few top-level variables
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(MAKEFILE_PATH)))

.PHONY: all
all: test format-code docs artifacts

.PHONY: qt
qt:
	uv run --group=dev python -m unittest discover --start-directory tests --verbose -b

.PHONY: test
test: check-code check-types qt

.PHONY: artifacts
artifacts: sdist wheel

.PHONY: sdist
sdist:
	uv build --sdist

.PHONY: wheel
wheel:
	uv build --wheel

.PHONY: check-types
check-types:
	uv run --group=dev mypy src/

.PHONY: format-code
format-code:
	@uv run ruff check --fix-only src/ tests/ docs/source/conf.py
	@uv run ruff format src/ tests/ docs/source/conf.py

.PHONY: check-code
check-code:
	@uv run ruff check src/ tests/ docs/source/conf.py

.PHONY: docs
docs:
	uv run --group=docs $(MAKE) -C docs html
	# $(IN_ENV) $(MAKE) -C docs html

.PHONY: publish
publish: artifacts
	uv publish dist/*

.PHONY: freeze
freeze:
	- uv pip freeze --color=auto

.PHONY: shell
shell:
	- uv run python

.PHONY: clean
clean:
	- @git clean -dfX >> /dev/null 2>&1
	- @rm -rf .env*
	- @rm -rf .venv*

.PHONY: git-clean
git-clean: clean
	- @git fsck
	- @git reflog expire --expire=now --all
	- @git repack -ad
	- @git prune
