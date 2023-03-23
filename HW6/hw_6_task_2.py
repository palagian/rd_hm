# 2. Створити функцію, яка сумує будь-яку кількість аргументів і повертає результат.

def sum_num(*args):
    for arg in args:
        #check if arguments are numbers
        if type(arg) == int or type(arg) == float:
            continue
        else:
            print(f"I can not sum your arguments. Use numbers only!")
            return None

    return sum(args)

print(sum_num(5, 4, 7, 21.1))

