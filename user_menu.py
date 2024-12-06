import user_class as u_c
import user_operations as u_o
import re

# Defining a function to display user operations menu and enable user interaction
def display_user_menu():
    print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
    user_input = input("Enter your choice: ").strip()
    if user_input == '1':
        name_input = input("Enter the user's name: ").title()
        id_input = input("Enter the user's library ID: ")
        if not u_o.check_user(name_input):
            if re.findall(r"^(\d{4})$", id_input):
                new_user = u_c.User(name_input, id_input)
                new_user.add_user()
            else:
                print("Invalid library ID.")
        else:
            print(f"{name_input} already exists in user database.")
    elif user_input == '2':
        name_input = input("Enter the user's name: ").title()
        if u_o.check_user(name_input):
            u_o.display_user(name_input)
        else:
            print(f"{name_input} does not exist in user database.")
    elif user_input == '3':
        u_o.display_users()
    else:
        print("Invalid input. Please try again.")