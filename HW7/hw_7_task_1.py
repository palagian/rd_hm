# 1. Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів
# add: додати запис
# delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі
# show <name>: детальна інформація по імені
#
# Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.

phone_book = [{"name": "Stepan Bandera", "phone": "+380501112233"},
              {"name": "Taras Schevchenko", "phone": "+380672223344"},
              {"name": "Yevhen Konovalets", "phone": "+380663332255"},
              {"name": "Lina Kostenko", "phone": "+380634441166"},
              {"name": "Bohdan Khmelnytskii", "phone": "+380675556677"}]

# function for calculation number of elements
def com_stats(phone_book):
    elements_number = len(phone_book)
    """return count of phone numbers"""
    return elements_number

# function for adding elements
def com_add(phone_book):
    new_contact = input(f"Please, enter name, surname and phone number (use space between): ")
    name, surname, phone = new_contact.split()
    """add a new contact to the phone book"""
    phone_book.append({"name": name + " " + surname, "phone": phone})
    """check if there is the same contact"""
    if phone_book.count({"name": name + " " + surname, "phone": phone}) != 1:
        print(f"This contact already exists!")
    else:
        return phone_book

# function for deleting element
def com_del(phone_book):
    index_del = input(f"Number of element you want to delete: ")
    index_del_int = int(index_del)
    phone_book.pop(index_del_int)
    """return phone book without chosen element"""
    return phone_book

# function for getting all names from the list
def com_names(phone_book):
    return phone_book[0]["name"], phone_book[1]["name"], phone_book[2]["name"], phone_book[3]["name"], phone_book[4]["name"]

# function for detailed data by name
def com_tel(phone_book):
    name = input("Write the name of the contact w/o surname: ")
    if name == "Stepan":
        return phone_book[0]["phone"]
    elif name == "Taras":
        return phone_book[1]["phone"]
    elif name == "Yevhen":
        return phone_book[2]["phone"]
    elif name == "Lina":
        return phone_book[3]["phone"]
    elif name == "Bohdan":
        return phone_book[4]["phone"]
    else:
        print(f"There is no contact with name {name}")

# phone book logic code
command = input("Your command is: ")

if command == "stats":
    print(com_stats(phone_book))
elif command == "add":
    print(com_add(phone_book))
elif command == "delete":
    print(com_del(phone_book))
elif command == "list":
    print(com_names(phone_book))
elif command == "show":
    print(com_tel(phone_book))
else:
    print(f"Command {command} is not available. Try again!")
