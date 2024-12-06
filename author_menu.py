import author_class as a_c
import author_operations as a_o
import re

# Defining a function to display author operations menu and enable user interaction
def display_author_menu():
    print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
    user_input = input("Enter your choice: ").strip()
    if user_input == '1':
        name_input = input("Enter the author's name: ").title()
        biography_input = input("Enter the author's biography: ").capitalize()
        if not a_o.check_author(name_input):
            new_author = a_c.Author(name_input, biography_input)
            new_author.add_author()
        else:
            print(f"{name_input} already exists in author database.")
    elif user_input == '2':
        name_input = input("Enter the author's name: ").title()
        if a_o.check_author(name_input):
            a_o.display_author(name_input)
        else:
            print(f"{name_input} not found in author database.")
    elif user_input == '3':
        a_o.display_authors()
    else:
        print("Invalid input. Please try again.")