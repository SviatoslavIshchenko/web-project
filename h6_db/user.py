from database import get_connection
from psycopg.errors import UniqueViolation


class User:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email

    def register(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (username, password, email)
                VALUES (%s, %s, %s)
                """,
                (self.username, self.password, self.email)
            )

            connection.commit()
            print("Користувача успішно зареєстровано!")

        except UniqueViolation:
            connection.rollback()
            print("Користувач з таким username або email вже існує!")

        finally:
            cursor.close()
            connection.close()

    def login(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT id
                FROM users
                WHERE username = %s AND password = %s
                """,
                (self.username, self.password)
            )

            user = cursor.fetchone()

            if user:
                return user[0]
            else:
                return None

        finally:
            cursor.close()
            connection.close()