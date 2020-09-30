"""
Defines the printexecutiontime decorator
"""
from datetime import datetime
from functools import wraps

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

def printexecutiontime(message, output=print, color=None):
    '''
    This function returns a decorator. This allows to have a decorator that accepts parameters.
    message: A string with a '{0}' placeholder for the time that will be sent to the console.
    '''
    def decorator(function):
        '''
        The decorator itself returns a wrapper function that will replace the original one.
        '''
        @wraps(function)
        def wrapper(*args, **kwargs):
            '''
            This wrapper calculates and displays the execution time of the function.
            '''
            start = datetime.utcnow()
            value = function(*args, **kwargs)
            elapsed = datetime.utcnow() - start
            msg = message.format(elapsed)
            if color:
                msg = color + msg + Fore.RESET
            output(msg)
            return value
        return wrapper
    return decorator
