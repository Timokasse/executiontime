"""
Defines the printexecutiontime decorator
"""

from datetime import datetime

def printexecutiontime(message, display=print):
    '''
    This function returns a decorator. This allows to have a decorator that accepts parameters.
    message: A string with a '{0}' placeholder for the time that will be sent to the console.
    '''
    def decorator(function):
        '''
        The decorator itself returns a wrapper function that will replace the original one.
        '''
        def wrapper(*args, **kwargs):
            '''
            This wrapper calculates and displays the execution time of the function.
            '''
            start = datetime.utcnow()
            value = function(*args, **kwargs)
            elapsed = datetime.utcnow() - start
            display(message.format(elapsed))
            return value
        return wrapper
    return decorator
