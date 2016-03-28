def printexecutiontime(message):
    '''
    This function returns a decorator. This allows to have a decorator that accepts parameters.
    meesage: A string with a '{0}' placeholder for the time that will be sent to the console.
    '''
    from datetime import datetime
    def decorator(function):
        '''
        The decorator itself returns a wrapper function that will replace the original one.
        '''
        def wrapper(*args, **kwargs):
            '''
            This wrapper calculates and displays the execution time of the function.
            '''
            start = datetime.now()
            value = function(*args, **kwargs)
            elapsed = datetime.now() - start
            print(message.format(elapsed))
            return value
        return wrapper
    return decorator
