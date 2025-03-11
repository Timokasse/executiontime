# executiontime

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Timokasse/executiontim/blob/master/LICENSE)

This module provides a simple function decorator to display its execution time on the console or in the logs.

## Installation

Simply install the package with `pip`:

```bash
pip install executiontime
```

## Usage

You simply need to decorate the function and specify a message template.
If you do not provide a message, one will be created for you based on the names of the decorated function and its module.

```python
from executiontime import printexecutiontime

@printexecutiontime("My function's execution took {0}")
def my_function():
    pass

if __name__ == '__main__':
    my_function()
```

By default, the message will be displayed on the console. But it is also possible to specify a log function, for example.

```python
from logging import info, INFO, basicConfig
from executiontime import printexecutiontime

@printexecutiontime("My function's execution took {0}", display=info)
def my_function():
    pass

if __name__ == '__main__':
    basicConfig(level=INFO)
    my_function()

```

It is also easy to add a little bit of color:

```python
from executiontime import printexecutiontime, LIGHTBLUE

@printexecutiontime("My function's execution took {0}", color=LIGHTBLUE)
def my_function():
    pass

if __name__ == '__main__':
    my_function()
```

## Changelog

- v0.4.1
  - The message is now optional and a default one is provided, based on the names of the decorated function and its module.
- v0.4.0
  - Refresh the dependencies
  - Replace deprecated datetime.utcnow()
