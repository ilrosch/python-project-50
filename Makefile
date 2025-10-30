install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

check: lint test

build:
	uv build

.PHONY: install test lint check build