# Development of ExecutionTime module

## Create development environment

We now have Poetry to setup the development environment:

```bash
poetry install
```

## Run the demo

Running the demo is very simple:

```bash
poetry run python demo.py
```

## Run the unit tests

Again with Poetry:

```bash
poetry run pytest tests
```

## Linter

We use `pylint`:

```bash
poetry run pylint executiontime
```

## Typing

We use `mypy`:

```bash
poetry run mypy executiontime
```
