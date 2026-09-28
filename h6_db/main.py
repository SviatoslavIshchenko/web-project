from database import create_tables
from user import User
from site_account import SiteAccount


create_tables()


while True:
    print("\n--- ГОЛОВНЕ МЕНЮ ---")
    print("1 - Зареєструватися")
    print("2 - Увійти")
    print("3 - Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        username = input("Введіть username: ")
        password = input("Введіть password: ")
        email = input("Введіть email: ")

        user = User(
            username=username,
            password=password,
            email=email
        )

        user.register()

    elif choice == "2":
        username = input("Введіть username: ")
        password = input("Введіть password: ")

        user = User(
            username=username,
            password=password
        )

        user_id = user.login()

        if user_id:
            print("Успішний вхід!")

            while True:
                print("\n--- МЕНЮ КОРИСТУВАЧА ---")
                print("1 - Додати сайт")
                print("2 - Показати мої сайти")
                print("3 - Вийти з облікового запису")

                user_choice = input("Оберіть дію: ")

                if user_choice == "1":
                    site_name = input("Введіть назву сайту: ")

                    print("\nОберіть вид входу:")
                    print("1 - Google")
                    print("2 - Apple")
                    print("3 - Facebook")
                    print("4 - Інший")

                    login_choice = input("Оберіть вид входу: ")

                    if login_choice == "1":
                        login_type = "Google"

                    elif login_choice == "2":
                        login_type = "Apple"

                    elif login_choice == "3":
                        login_type = "Facebook"

                    elif login_choice == "4":
                        login_type = "Other"

                    else:
                        print("Неправильний вид входу.")
                        continue

                    if login_type == "Other":
                        site_login = input("Введіть логін на сайті: ")
                        site_password = input("Введіть пароль на сайті: ")

                        account = SiteAccount(
                            site_name=site_name,
                            login_type=login_type,
                            user_id=user_id,
                            login=site_login,
                            password=site_password
                        )

                    else:
                        account = SiteAccount(
                            site_name=site_name,
                            login_type=login_type,
                            user_id=user_id
                        )

                    account.save()

                elif user_choice == "2":
                    accounts = SiteAccount.show_accounts(user_id)

                    print("\n--- МОЇ САЙТИ ---")

                    if not accounts:
                        print("У вас ще немає збережених сайтів.")

                    else:
                        for account in accounts:
                            site_name, login, password, login_type = account

                            print(f"\nСайт: {site_name}")
                            print(f"Вид входу: {login_type}")

                            if login_type == "Other":
                                print(f"Логін: {login}")
                                print(f"Пароль: {password}")

                elif user_choice == "3":
                    print("Вихід з облікового запису.")
                    break

                else:
                    print("Невідома команда.")

        else:
            print("Неправильний логін або пароль!")

    elif choice == "3":
        print("Програму завершено.")
        break

    else:
        print("Невідома команда. Спробуйте ще раз.")