# 3. (необов'язкове виконання) Створити клас MyStr(str), який має перевизначтити метод str таким чином, щоб замість друку
# реального значення всі літери були переведені в верхній регістр:

# my_str = MyStr('test')
# print(my_str)
# >>> "TEST"

class MyStr(str):
    def __str__(self):
        return super().__str__().upper()

my_str = MyStr('test')
print(my_str)
