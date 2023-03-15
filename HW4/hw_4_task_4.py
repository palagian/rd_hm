# Завдання:
# 4. (необов'язкове виконання) Створити програму, яка буде очікувати введення тексту від користувача і повідомляти
# якого типу введені дані. Використати match, case і вбудовані функції Python

text = input("Enter some text ")

match text.isalpha():
    case True:
        print(f"'{text}' is a string")
    case False:
        match text.isdigit():
            case True:
                print(f"{text} is a number")
            case _:
                print(f"Please, use numbers or letters only. No spaces. Thank you!")