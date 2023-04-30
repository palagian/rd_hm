# 2. (необов'язкове виконання) Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на *@*.

import re
import sys

# reading file's name
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Please enter file's name: ")

# opening and reading file
with open(filename, "r") as file:
    text = file.read()

# searching for emails with regex
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(pattern, text)

# swithing emails for *@*
for email in emails:
    text = text.replace(email, '*@*')

# showing changing text
print(text)