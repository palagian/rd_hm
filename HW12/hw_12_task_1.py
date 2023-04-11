# 1. Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана. Декоратор має працювати для різних функцій однаково.

import time

def my_decorator(func):
    # decorator logic
    called_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    def wraper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called on {called_time}")
        res = func(*args, **kwargs)
        return res
    return wraper

@my_decorator
def my_func():
    # function w/o parameters
    print("This is my func")

@my_decorator
def add_num(a, b):
    # function with parameters and returning some result
    return a + b

@my_decorator
def my_other_func(a, b, c, city):
    # function with parameters
    print(a, b, c, city)

my_func()
print(add_num(1, 2))
my_other_func(1, 2, 3, city="Kyiv")