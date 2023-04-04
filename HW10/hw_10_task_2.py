# 2. (необов'язкове виконання) Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі, використовуючи рекурсію.

def fibonacci(n):
    a = 1
    if n > 2:
        a = fibonacci(n-1) + fibonacci(n-2)
    return a

user_number = input(f"Enter you number: ")

if user_number.isdigit():
    value = fibonacci(int(user_number))
    print(f"{user_number} element in the Fibonacci sequence is equal to {value}")
else:
    print(f"{user_number} is not a number! Try again!")



