from connect_mysql import connect_database
from book_class import Book

# Defining a function to check the existence of the selected book in the library
def check_book(title_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(query, (title_input,))
            if cursor.fetchall():
                return True
            else:
                return False

        finally:
            cursor.close()
            conn.close()

# Defining a function to check the availability of the selected book
def check_availability(title_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT availability FROM books WHERE title = %s"
            cursor.execute(query, (title_input,))
            if cursor.fetchone()[0] == 1:
                return True
            else:
                return False

        finally:
            cursor.close()
            conn.close()

# Defining a function to display all books with their details
def display_books():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            books = cursor.fetchall()
        
            if books:
                print("Books in library:")
                for book in books:
                    query = "SELECT name FROM authors WHERE id = %s"
                    cursor.execute(query, (book[2],))
                    author = cursor.fetchone()[0]
                    print(f"Title: {book[1]}, Author: {author}, ISBN {book[3]}, Publication Date: {book[4]}, Availability Status: {"Available" if book[5] == 1 else "Borrowed"}")
            else:
                print("Library contains no books.")
        
        finally:
            cursor.close()
            conn.close()

# Defining a function to display the details of the selected book
def display_book(title_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(query, (title_input,))
            book = cursor.fetchone()

            query = "SELECT name FROM authors WHERE id = %s"
            cursor.execute(query, (book[2],))
            author = cursor.fetchone()[0]
            print(f"Title: {book[1]}, Author: {author}, ISBN {book[3]}, Publication Date: {book[4]}, Availability Status: {"Available" if book[5] == 1 else "Borrowed"}")
        
        finally:
            cursor.close()
            conn.close()

# Defining a function to borrow the selected book from the library
def borrow_book(title_input, name_input, borrow_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "UPDATE books SET availability = 0 WHERE title = %s"
            cursor.execute(query, (title_input,))
            conn.commit()
        
            query = "SELECT id FROM users WHERE name = %s"
            cursor.execute(query, (name_input,))
            user_id = cursor.fetchone()[0]
            query = "SELECT id FROM books WHERE title = %s"
            cursor.execute(query, (title_input,))
            book_id = cursor.fetchone()[0]

            borrowed_book = (user_id, book_id, borrow_input)
            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
            cursor.execute(query, borrowed_book)
            conn.commit()
            print(f"{title_input} borrowed from library.")

        finally:
            cursor.close()
            conn.close()

# Defining a function to return the selected book to the library
def return_book(title_input, name_input, return_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "UPDATE books SET availability = 1 WHERE title = %s"
            cursor.execute(query, (title_input,))
            conn.commit()
              
            query = "SELECT id FROM users WHERE name = %s"
            cursor.execute(query, (name_input,))
            user_id = cursor.fetchone()[0]
            query = "SELECT id FROM books WHERE title = %s"
            cursor.execute(query, (title_input,))
            book_id = cursor.fetchone()[0]

            query = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s and book_id = %s"
            cursor.execute(query, (return_input, user_id, book_id))
            conn.commit()
            print(f"{title_input} returned to library.")
        
        finally:
            cursor.close()
            conn.close()

check_availability('1984')