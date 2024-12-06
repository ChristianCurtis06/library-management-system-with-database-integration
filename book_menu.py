import book_class as b_c
import book_operations as b_o
import author_operations as a_o
import user_operations as u_o
import re

# Defining a function to display book operations menu and enable user interaction
def display_book_menu():
    print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
    user_input = input("Enter your choice: ").strip()
    if user_input == '1':
        title_input = input("Enter the book's title: ").title()
        author_input = input("Enter the book's author: ").title()
        isbn_input = input("Enter the book's ISBN: ")
        publication_input = input("Enter the book's publication date (YYYY-MM-DD): ")
        if not b_o.check_book(title_input):
            if re.findall(r"^(97[89])\d{9}(\d|X)$", isbn_input) and re.findall(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", publication_input):
                if a_o.check_author(author_input):
                    new_book = b_c.Book(title_input, author_input, isbn_input, publication_input)
                    new_book.add_book()
                else:
                    print(f"{author_input} not found in database.")
            else:
                print("Invalid ISBN or publication date.")
        else:
            print(f"{title_input} already exists in library.")
    elif user_input == '2':
        title_input = input("Enter the book's title: ").title()
        if b_o.check_book(title_input):
            if b_o.check_availability(title_input):
                name_input = input("Enter the user's name: ").title()
                if u_o.check_user(name_input):
                    borrow_input = input("Enter the book's borrow date (YYYY-MM-DD): ")
                    if re.findall(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", borrow_input):
                        b_o.borrow_book(title_input, name_input, borrow_input)
                    else:
                        print("Invalid borrow date.")
                else:
                    print(f"{name_input} does not exist in database.")
            else:
                print(f"{title_input} is already borrowed.")
        else:
            print(f"{title_input} does not exist in library.")
    elif user_input == '3':
        title_input = input("Enter the book's title: ").title()
        if b_o.check_book(title_input):
            if not b_o.check_availability(title_input):
                name_input = input("Enter the user's name: ").title()
                if u_o.check_user(name_input):
                    return_input = input("Enter the book's return date (YYYY-MM-DD): ")
                    if re.findall(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", return_input):
                        b_o.return_book(title_input, name_input, return_input)
                    else:
                        print("Invalid return date.")
                else:
                    print(f"{name_input} does not exist in database.")
            else:
                print(f"{title_input} was not borrowed.")
        else:
            print(f"{title_input} does not exist in library.")
    elif user_input == '4':
        title_input = input("Enter the book's title: ").title()
        if b_o.check_book(title_input):
            b_o.display_book(title_input)
        else:
            print(f"{title_input} does not exist in library.")
    elif user_input == '5':
        b_o.display_books()
    else:
        print("Invalid input. Please try again.")