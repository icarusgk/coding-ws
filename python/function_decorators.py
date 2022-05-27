# Decorator is a structural design pattern that allows programmers to extend
# and modify the behavior of a function, a method, or a class without
# changing their code.

# Decorators are just wrappers around the initial objects. Most frequently, we
# use them to pass a function as an argument to a decorator to call this
# function later and perform some action before and after the call.

# In Python, the std syntax for decorators is the @ sign preceding the name of
# a decorator, and then the object we want to decorate on the next line with
# the same indentation.
# Decorators are called immediately before the body of a function, the behavior
# of which we would like to change.

# Example
def our_decorator(other_func):
    def wrapper(args_for_function):
        print('This happens before we call the function')
        # Returns the originally modified function
        return other_func(args_for_function)
    return wrapper


@our_decorator
def greet(name):
    print('Hello,', name)


greet('Roger')


# Case in which we want to use decorators
import time
def func1(args_for_function):
    start = time.time()
    print('hiii')
    end = time.time()
    print('func1 takes', end - start, 'seconds')

def func2(args_for_function):
    start = time.time()
    print('hiii')
    end = time.time()
    print('func2 takes', end - start, 'seconds')

# The problem here is that These lines would be redundant to the actual
# functionality and the initial code.


# We can make them reusable
def timer(func):
    def wrapper(args_for_function):
        start = time.time()
        func(args_for_function)
        end = time.time()
        print('func takes', end - start, 'seconds')
    return wrapper


@timer
def func3(args_for_function):
    pass


def tagged(func):
    def wrapper(inp):
        text = func(inp)
        return f'<title>{text}</title>'
    return wrapper


@tagged
def from_input(inp):
    string = inp.strip()
    return string


print(from_input('roger'))


def to_upper(function):
    def wrapper(args):
        return function(args).upper()
    return wrapper

