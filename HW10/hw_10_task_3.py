# 3. (необов'язкове виконання) Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію.

def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n-1)

user_number = input(f"Enter you number: ")

if user_number.isdigit():
    value = factorial(int(user_number))
    print(f"Factorial of {user_number} is {value}")
else:
    print(f"{user_number} is not a number! Try again!")