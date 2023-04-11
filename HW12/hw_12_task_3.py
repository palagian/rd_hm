# 3. (необов'язкове виконання) Переписати декоратор із першого завдання, щоб він приймав цілочисельний аргумент `times`.
# Стільки разів виконувавати друк назви функції і часу, скільки ‘times’ задано.

import time

times = input("Enter your number: ")

def my_decorator(func):
    # decorator logic
    called_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    def wraper(*args, **kwargs):
        try:
            times.isdigit()
            print(f"Function '{func.__name__}' was called on {called_time}\n" * int(times))
            res = func(*args, **kwargs)
            return res
        except ValueError:
            print(f"'{times}' is not a number! Try again!")
    return wraper

@my_decorator
def my_func():
    # function w/o parameters
    print("This is my func\n")

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