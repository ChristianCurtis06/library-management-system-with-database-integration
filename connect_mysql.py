import mysql.connector
from mysql.connector import Error

# Defining a function to connect the python script to the MySQL database 'library_management_db'
def connect_database():
    database = "library_management_db"
    user = "root"
    password = "********"
    host = "*********"

    try:
        conn = mysql.connector.connect(
            database = database,
            user = user,
            password = password,
            host = host
        )
        return conn

    except Error as e:
        print(f"Error: {e}")
        return None