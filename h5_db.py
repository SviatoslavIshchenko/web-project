import sqlite3


conn = sqlite3.connect("users.db")

cursor = conn.cursor()


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def register(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (username, password, email)
                VALUES (?, ?, ?)
                """,
                (self.username, self.password, self.email)
            )

            conn.commit()
            print("Користувача успішно зареєстровано!")

        except sqlite3.IntegrityError:
            print("Користувач з таким username або email вже існує!")

        finally:
            conn.close()

    def login(self, username, password):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username = ? AND password = ?
            """,
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        return user is not None

while True:

    print("\n1 - Зареєструватися")
    print("2 - Увійти")
    print("3 - Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")

        user = User(username, password, email)
        user.register()

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")

        user = User("", "", "")

        if user.login(username, password):
            print("Успішний вхід!")
        else:
            print("Неправильні дані!")

    elif choice == "3":
        print("Роботу програми завершено.")
        break

    else:
        print("Невідома команда.")
