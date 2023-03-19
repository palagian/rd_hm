# Завдання:
# 1. Створити програму, яка буде очікувати від користувача введення тексту і виведе інформацію по кожному надрукованому символу:
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”

text = input("Enter some text ")
symbol = list(text)
print(f"{symbol}")

for i in symbol:
    # check if it's a letter - uppercase / lowercase
    if i.isalpha():
        print(f"'{i}' is a letter")
        if i.isupper():
            print(f"'{i}' is an uppercase letter")
        else:
            print(f"'{i}' is a lowercase letter")
        continue
    # check if it's a number - even / odd
    elif i.isdigit():
        print(f"'{i}' is a number")
        if int(i) % 2 == 0:
            print(f"'{i}' is an even number")
        else:
            print(f"'{i}' is an odd number")
        continue
    # if it's not a letter and not a number, it's a symbol
    else:
        print(f"'{i}' is a symbol")
