# 1. Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.

def recursion (n):
    if n == -1:
        return n
    print(n)
    return recursion(n-1)


user_number = input(f"Enter you number: ")

if user_number.isdigit():
    recursion(int(user_number))
else:
    print(f"{user_number} is not a number! Try again!")
