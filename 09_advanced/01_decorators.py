"""
DECORATORS — one of the TOP Python interview questions.
No direct JS equivalent (closest: Higher-Order Components in React,
or middleware functions in Express — conceptually similar!).

A decorator is a FUNCTION that takes a function and returns a
new function with extra behavior wrapped around it.

Think of Express middleware:
    app.use((req, res, next) => { console.log("Request received"); next(); })
Decorators do something similar — they "wrap" behavior around your function.
"""

import time
import functools


def my_decorator(func):
    @functools.wraps(func)         # preserves original function's name/docstring (best practice)
    def wrapper(*args, **kwargs):   # accepts ANY arguments the original function needs
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)   # call the original function
        print(f"After calling {func.__name__}")
        return result
    return wrapper


@my_decorator          # this line is SHORTHAND for: say_hello = my_decorator(say_hello)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Rahul")

# --- A real, practical decorator: timing a function ---
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
    return "done"

slow_function()

# --- Decorators WITH arguments (a decorator factory) ---
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def greet():
    print("Hi!")

greet()   # prints "Hi!" 3 times

# --- Built-in decorators you'll see everywhere ---
class Example:
    @staticmethod
    def util():
        pass

    @property
    def computed_value(self):
        return 42

# INTERVIEW: Decorators work because Python functions are FIRST-CLASS objects
# — they can be passed around and returned just like any other value
# (you already know this from JS higher-order functions / callbacks!)

# TODO (practice): write a `@log_arguments` decorator that prints out
# every argument passed to the decorated function before calling it.
