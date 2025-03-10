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

## Deploying a new version on PyPI

There is no CI/CD in place for `executiontime`. The publishing will be done manually with the help of the script `publish.sh`.

It requires a PyPI API token and store it in `PYPI_API_TOKEN` environment variable with the help of the `secrets.sh` file not to be stored in the git repository.

In order to publish the next patch version, directly call the script:

```bash
./publish.sh
```

For example, if the latest version of `executiontime` was `0.3.6`, it will create a new `0.3.7`.

If you want to change the minor or major version, you will have to use the `poetry version` and then commit your changes command before doing the publish.

```bash
poetry version minor
git add .
git commit -m 'New minor version'
git push
./publish.sh
```
