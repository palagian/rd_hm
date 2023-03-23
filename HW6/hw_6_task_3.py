# 3. (необов'язкове виконання) Знайти найбільший елемент масиву
# — використати built-in функцію
# — створити свою функцію
# — використати лямбда функцію

from array import *

numbers = array('i', [10, 77, 20, 89, 40,])

# built-in function
def max_num_1(numbers):
    return max(numbers)

print(f"Built-in function says, max number in the array is: {max_num_1(numbers)}")

#my function
def max_num_2(numbers):
    my_max_num = numbers[0]
    for num in numbers:
        if num > my_max_num:
            my_max_num = num
    return my_max_num

print(f"My function says, max number in the array is: {max_num_2(numbers)}")

#lambda function
max_num_3 = lambda x: max(numbers)
print(f"Lambda function says, max number in the array is: {max_num_3(numbers)}")