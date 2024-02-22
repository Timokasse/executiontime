"""
Some unit tests for the executiontime package
"""

from time import sleep
from unittest import TestCase, main
from unittest.mock import MagicMock

from executiontime import printexecutiontime

# pylint: disable=missing-class-docstring, missing-function-docstring


class TestExecutionTime(TestCase):

    def test_decorator(self):
        @printexecutiontime("Time spent: {0}")
        def my_function():
            """Just a little sleep"""
            sleep(0.1)

        self.assertEqual(my_function.__name__, "my_function")
        self.assertEqual(my_function.__doc__, "Just a little sleep")

    def test_output(self):
        output = MagicMock()

        @printexecutiontime("Time spent: {0}", output=output)
        def my_function():
            """Just a little sleep"""
            sleep(0.1)

        my_function()
        self.assertEqual(output.call_count, 1)
        self.assertEqual(len(output.call_args.args), 1)
        self.assertEqual(output.call_args.args[0][:11], "Time spent:")


if __name__ == "__main__":
    main()
