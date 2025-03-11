"""
Basic demo program for the executiontime decorator.
"""

from time import sleep
from logging import basicConfig, info, INFO

from executiontime import printexecutiontime, LIGHTBLACK, LIGHBLUE, RED


@printexecutiontime("Test function executes in {0}", color=LIGHTBLACK)
def my_function() -> None:
    """
    The function we want to know the execution time of.
    """
    sleep(0.5)


@printexecutiontime("Test function executes in {0}", color=LIGHBLUE, output=info)
def my_function_info() -> None:
    """
    The function we want to know the execution time of.
    """
    sleep(0.3)


@printexecutiontime(color=RED)
def my_function_no_message() -> None:
    """
    The function we want to know the execution time of."
    """
    sleep(0.7)


if __name__ == "__main__":
    basicConfig(level=INFO)
    my_function()
    my_function_info()
    my_function_no_message()
