# task_1: Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
moto = "I love Python"
print((moto + " ") * 42)

# task_2: Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.
age_in_month = 434

# task_3: Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
age_in_years = age_in_month / 12
print(age_in_years)

# task_4: Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”, де на замість пропусків
# буде підставлятись ваші імʼя та вік. Значення віку слід брати зі змінної age_in_years.
name = "Anastasiia"
my_age = "Му name is " + str(name) + " I’m " + str(int(age_in_years)) + " years old"
print(my_age)

# task_5: Створити змінну зі значенням 1. Використовуючи оператори порівняння, порівняти її із будь-якими іншими
# значеннями (мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.
i = 1
print(i == 6)
print(i != 2)
print(i > 10)
print(i < 10)
print(i >= 1)
print(i <= 5)

#task_6: Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d, значення якої має бути “256”
a = 2
b = 5
c = 6
d = (b * c + a) * (a + c)
print(d)



