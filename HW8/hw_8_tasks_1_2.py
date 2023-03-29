# 1. Написати функцію, яка повертає тільки однакові елементи двох множин.
# 2. Написати функцію, яка повертає тільки унікальні елементи двох множин.

set1 = set([1, 4, 8, 15, 22, 59, 93])
set2 = set([3, 15, 99, 8, 22, 112, 66])

# looking for common elements in set1 and set2
common_elements = set1.intersection(set2)

# looking for unique elements in set1 and set2
union_set = set1.union(set2)

print(common_elements)
print(union_set)