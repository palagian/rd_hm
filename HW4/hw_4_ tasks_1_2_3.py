# Завдання:
# 1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти — чи є введений текст
# “числом” чи “словом” (використати функцію cтрічки .isdigit() або .isalpha())
# 2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
# 3. Якщо це “слово”, програма має вказати його довжину.

text = input("Enter some text ")

# check if text is a string (tasks 1 and 3)
if text.isalpha():
    print(f"'{text}' is a string")
    print(f"Your text has {len(text)} characters")
# check if text is a number (tasks 1 and 2)
elif text.isdigit():
    print(f"{text} is a number")
    # check if text is odd or even (task 2)
    if int(text) % 2 == 0:
        print(f"{text} is an even number")
    else:
        print(f"{text} is an odd number")
else:
    print(f"Please, use numbers or letters only. No spaces. Thank you!")
