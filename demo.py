#!/usr/bin/env python
"""
Basic demo program for the executiontime decorator.
"""

from time import sleep
from logging import basicConfig, info, INFO

from executiontime import printexecutiontime

@printexecutiontime('Test function executes in {0}')
def myfunction():
    """
    The function we want to know the execution time of.
    """
    sleep(0.5)

@printexecutiontime('Test function executes in {0}', display=info)
def myfunction2():
    """
    The function we want to know the execution time of.
    """
    sleep(0.3)

if __name__ == '__main__':
    basicConfig(level=INFO)
    myfunction()
    myfunction2()
