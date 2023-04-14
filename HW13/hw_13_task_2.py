# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.

import time
import json

def my_decorator(func):
    # decorator logic
    called_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    json_file = json.dumps(called_time)
    function_name = func.__name__

    def wraper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called on {called_time}")
        res = func(*args, **kwargs)
        # write data into json file
        with open("json_date.json", "a") as file:
            file.write(function_name + " was called on  " + json_file + "\n")
        return res
    return wraper


@my_decorator
def first_function():
    # function w/o parameters
    return None


@my_decorator
def second_function():
    # function w/o parameters
    return None


first_function()
second_function()
