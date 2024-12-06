from connect_mysql import connect_database
from author_class import Author

# Defining a function to check the existence of the selected author in the database
def check_author(name_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM authors WHERE name = %s"
            cursor.execute(query, (name_input,))
            if cursor.fetchall():
                return True
            else:
                return False

        finally:
            cursor.close()
            conn.close()

# Defining a function to display all authors with their details
def display_authors():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM authors"
            cursor.execute(query)
            authors = cursor.fetchall()
            if authors:
                print("Authors in database:")
                for author in authors:
                    print(f"Name: {author[1]}, Biography: {author[2]}")
            else:
                print("Database contains no authors.")
        
        finally:
            cursor.close()
            conn.close()

# Defining a function to display the details of the selected author
def display_author(name_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM authors WHERE name = %s"
            cursor.execute(query, (name_input,))
            author = cursor.fetchone()
            print(f"Name: {author[1]}, Biography: {author[2]}")
        
        finally:
            cursor.close()
            conn.close()