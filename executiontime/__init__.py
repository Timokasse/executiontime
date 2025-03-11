"""
Defines the printexecutiontime decorator
"""

from datetime import datetime
from functools import wraps
from typing import Callable, ParamSpec, Optional, TypeVar

from colorama import Fore

BLACK = Fore.BLACK
BLUE = Fore.BLUE
CYAN = Fore.CYAN
GREEN = Fore.GREEN
LIGHTBLACK = Fore.LIGHTBLACK_EX
LIGHBLUE = Fore.LIGHTBLUE_EX
LIGHTCYAN = Fore.LIGHTCYAN_EX
LIGHTGREEN = Fore.LIGHTGREEN_EX
LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX
LIGHTRED = Fore.LIGHTRED_EX
LIGHTWHITE = Fore.LIGHTWHITE_EX
LIGHTYELLOW = Fore.LIGHTYELLOW_EX
MAGENTA = Fore.MAGENTA
RED = Fore.RED
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW

P = ParamSpec("P")
T = TypeVar("T")


def printexecutiontime(
    message: Optional[str] = None, output: Callable[..., None] = print, color: Optional[str] = None
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    This function returns a decorator. This allows to have a decorator that accepts parameters.
    message: A string with a '{0}' placeholder for the time that will be sent to the console.
        If none is provided, we will use a default message with the module's and functions's names.
    output: A function to send the message. By default we use 'print' that sends the message to the console.
    color: One of the constant string provided in this module to color the message.
    """

    def decorator(function: Callable[P, T]) -> Callable[P, T]:
        """
        The decorator itself returns a wrapper function that will replace the original one.
        """

        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            """
            This wrapper calculates and displays the execution time of the function.
            """
            start = datetime.now()
            value = function(*args, **kwargs)
            elapsed = datetime.now() - start
            if message is None:
                msg = f"{function.__module__}.{function.__name__} executed in {elapsed}"
            else:
                msg = message.format(elapsed)
            if color:
                msg = color + msg + Fore.RESET
            output(msg)
            return value

        return wrapper

    return decorator
