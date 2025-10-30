install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff

check: lint test

build:
	uv build

.PHONY: install test lint check build