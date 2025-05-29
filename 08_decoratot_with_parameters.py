'''
A decorator with parameters is essentially a function that returns a decorator. 
This allows you to pass arguments to the decorator, which can be useful for customizing its behavior.
'''

from functools import wraps

def repeat(times):
    # This is a decorator factory function that takes a parameter 'times',
    # which specifies how many times the decorated function should be called.
    def decorator(func):
        # This is the actual decorator function that takes the function 'func'
        # to be decorated as its argument.
        @wraps(func)
        def wrapper(*args, **kwargs):
            # The wrapper function executes the original function 'func'
            # the specified number of times ('times').
            # It uses *args and **kwargs to pass any arguments and keyword arguments to 'func'.
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Example usage:
@repeat(3)  # The 'greet' function is decorated with @repeat(3),
            # which means it will print the greeting three times when called.
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
