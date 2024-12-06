from connect_mysql import connect_database
import author_operations as a_o

# Class module containing 'Book' class with its object methods
class Book:
    def __init__(self, title, author, isbn, publication):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication = publication
        self.__availability = 1

    def add_book(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT id FROM authors WHERE name = %s"
                cursor.execute(query, (self.__author,))
                author_id = cursor.fetchone()[0]
                new_book = (self.__title, author_id, self.__isbn, self.__publication, self.__availability)

                query = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, new_book)
                conn.commit()
                print(f"{self.__title} added to library.")

            finally:
                cursor.close()
                conn.close()