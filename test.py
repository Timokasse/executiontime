#!/usr/bin/env python

from time import sleep

from executiontime import printexecutiontime

@printexecutiontime('Test function executes in {0}')
def myfunction():
    sleep(2)

if __name__ == '__main__':
    myfunction()
