include .Makefile.in

.PHONY: all
all: test format-code docs artifacts  ## Run tests, formatter, build docs & artifacts

.PHONY: unittests
unittests:  ## Run the unittest suite
	uv run --group=dev python -m unittest discover --start-directory tests --verbose -b

.PHONY: test
test: check-code check-types unittests  ## Run linter, type checker, and unittests

.PHONY: artifacts
artifacts: sdist wheel  ## Build project in all packaging formats

.PHONY: sdist
sdist:  ## Package the project in sdist format
	uv build --sdist

.PHONY: wheel
wheel:  ## Package the project as a wheel file
	uv build --wheel

.PHONY: mypy
mypy:  ## Type check using mypy
	uv run --group=dev mypy src/

.PHONY: ty
ty:  ## Type check using ty
	uv run --group=dev ty check src/

.PHONY: check-types
check-types: mypy ty ## Type-check the project

.PHONY: format-code
format-code:  ## Format the code
	@uv run ruff check --fix-only src/ tests/ docs/source/conf.py
	@uv run ruff format src/ tests/ docs/source/conf.py

.PHONY: check-code
check-code:  ## Run linter checks
	@uv run ruff check src/ tests/ docs/source/conf.py

.PHONY: docs
docs:  ## Build documentation
	uv run --group=docs $(MAKE) -C docs html
	# $(IN_ENV) $(MAKE) -C docs html

.PHONY: publish
publish: artifacts  ## Publish build artifacts
	uv publish dist/*

.PHONY: freeze
freeze:  ## Display packages installed in the virtual environment
	- uv pip freeze --color=auto

.PHONY: shell
shell:  ## Launch an interactive Python shell
	- uv run python

.PHONY: clean
clean:  ## Cleanup the workspace and remove the virtual environment
	- @git clean -dfX >> /dev/null 2>&1
	- @rm -rf .env*
	- @rm -rf .venv*

.PHONY: git-clean
git-clean: clean  ## Cleanup your local git repository
	- @git fsck
	- @git reflog expire --expire=now --all
	- @git repack -ad
	- @git prune
