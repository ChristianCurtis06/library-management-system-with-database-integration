from connect_mysql import connect_database

# Class module containing 'Author' class with its object methods
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def add_author(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                new_author = (self.__name, self.__biography)

                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
                cursor.execute(query, new_author)
                conn.commit()
                print(f"{self.__name} added to database.")

            finally:
                cursor.close()
                conn.close()

    def view_author_details(self):
        print(f"Name: {self.__name}, Biography: {self.__biography}")