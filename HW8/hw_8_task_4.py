# 4. (необов'язкове виконання) Вивести всі елементу масиву, які є числом, використовуючи filter.

lst = [1, 'cat', 2, 'dog', 3, 'rabbit', 4, 'cow', 5]

def numbers(element):
    if type(element) == int:
        return element

for element in filter(numbers, lst):
    print(element)