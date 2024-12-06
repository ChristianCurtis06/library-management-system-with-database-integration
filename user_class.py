from connect_mysql import connect_database

# Class module containing 'User' class with its object methods
class User:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    
    def add_user(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                new_user = (self.__name, self.__id)

                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
                cursor.execute(query, new_user)
                conn.commit()
                print(f"{self.__name} added to database.")

            finally:
                cursor.close()
                conn.close()