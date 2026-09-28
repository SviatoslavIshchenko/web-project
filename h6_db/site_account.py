from database import get_connection


class SiteAccount:
    def __init__(
        self,
        site_name,
        login_type,
        user_id,
        login=None,
        password=None
    ):
        self.site_name = site_name
        self.login_type = login_type
        self.user_id = user_id
        self.login = login
        self.password = password

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO site_accounts
                    (site_name, login, password, login_type, user_id)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    self.site_name,
                    self.login,
                    self.password,
                    self.login_type,
                    self.user_id
                )
            )

            connection.commit()
            print("Інформацію про сайт успішно збережено!")

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def show_accounts(user_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT site_name, login, password, login_type
                FROM site_accounts
                WHERE user_id = %s
                """,
                (user_id,)
            )

            accounts = cursor.fetchall()

            return accounts

        finally:
            cursor.close()
            connection.close()
