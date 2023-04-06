# 2. (необов'язкове виконання) Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occurred".

class MyCustomException(Exception):
    """ my custom exception class """

try:
    raise MyCustomException('Custom exception is occurred')
except MyCustomException as ex:
    print(ex)

