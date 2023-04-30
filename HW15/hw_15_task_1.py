# 1. До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX

import re


phone_book = [{"name": "Stepan Bandera", "phone": "+380501112233"},
              {"name": "Taras Schevchenko", "phone": "+380672223344"},
              {"name": "Yevhen Konovalets", "phone": "+380663332255"},
              {"name": "Lina Kostenko", "phone": "+380634441166"},
              {"name": "Bohdan Khmelnytskii", "phone": "+380675556677"}]


def com_stats(phone_book):
    """ function for calculation number of elements """
    elements_number = len(phone_book)
    # return count of phone numbers
    return elements_number

def com_add(phone_book):
    # try... except... else... to check if user enters required keys"""
    try:
        # add a new contact to the phone book """
        new_contact = input(f"Please, enter name, surname and phone number (use space between): ")
        name, surname, phone = new_contact.split()
    except (ValueError):
        print(f"Your entry is incorrect. Please, enter name, surname and phone!")
    else:
        # validate phone number using RegEx
        pattern = r'^(\+?38)?(0\d{9})$'
        if not re.match(pattern, phone):
            print("Invalid phone number. Please enter a valid phone number.")
            return phone_book
        # normalize phone number to international format
        if phone.startswith('0'):
            phone = '+38' + phone
        elif phone.startswith('380'):
            phone = '+' + phone
        phone_book.append({"name": name + " " + surname, "phone": phone})
        # check if there is the same contact
        if phone_book.count({"name": name + " " + surname, "phone": phone}) != 1:
            print(f"This contact already exists!")
        else:
            return phone_book


def com_del(phone_book):
    """ function for deleting element """
    index_del = input(f"Number of element you want to delete: ")
    index_del_int = int(index_del)
    phone_book.pop(index_del_int)
    # return phone book without chosen element
    return phone_book


def com_names(phone_book):
    """ function for getting all names from the list """
    for phone_row in phone_book:
        print(phone_row["name"])

def com_tel(phone_book):
    """ function for detailed data by name """
    name = input("Write the name of the contact w/o surname: ")
    for phone_row in phone_book:
        if phone_row["name"].split()[0] == name:
            print(phone_row["phone"])
        else:
            continue

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