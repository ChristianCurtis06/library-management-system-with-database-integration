from connect_mysql import connect_database
from user_class import User

# Defining a function to check the existence of the selected user in the database
def check_user(name_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE name = %s"
            cursor.execute(query, (name_input,))
            if cursor.fetchall():
                return True
            else:
                return False

        finally:
            cursor.close()
            conn.close()

# Defining a function to display all users with their details
def display_users():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            users = cursor.fetchall()
            if users:
                print("Users in database:")
                for user in users:
                    print(f"Name: {user[1]}, Library ID: {user[2]}")
            else:
                print("Database contains no users.")
        
        finally:
            cursor.close()
            conn.close()

# Defining a function to display the details of the selected user
def display_user(name_input):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE name = %s"
            cursor.execute(query, (name_input,))
            user = cursor.fetchone()
            print(f"Name: {user[1]}, Library ID: {user[2]}")
        
        finally:
            cursor.close()
            conn.close()