PYTHON=python3

setup: setup-qa
	$(PYTHON) -m venv .venv
	. .venv/bin/activate && pip install -r requirements.in
.PHONY: setup

validate:
	pre-commit run --all-files
.PHONY: validate

test:
	. .venv/bin/activate && python -m pytest tests
.PHONY: test
