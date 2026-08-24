"""
Опис: Створіть набір декораторів, які автоматично перевірятимуть функції на наявність можливих помилок під час їх виконання.

Кроки:
"""

"""
1. Створіть декоратор @check_division_error, який перевіряє, чи немає ділення на нуль в функціях. 
Якщо при виклику функції сталася помилка ділення на нуль, декоратор повинен вивести повідомлення про помилку та завершити виконання програми.
"""

from functools import wraps


def check_division_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ZeroDivisionError:
            print("Помилка: ділення на нуль.")
            raise

    return wrapper


"""
Створіть декоратор @check_index_error, який перевіряє, чи виходить індекс за межі списку при доступі до елементу. 
Якщо при виклику функції сталася помилка індексації, декоратор повинен вивести повідомлення про помилку та завершити виконання програми.
"""
def check_index_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except IndexError:
            print("Помилка: індекс виходить за межі списку.")
            raise

    return wrapper


"""
3. Створіть функцію divide, яка приймає два числа a та b і повертає результат ділення a на b. 
Додайте декоратор @check_division_error до цієї функції.
"""
@check_division_error
def divide(a, b):
    return a / b

"""
4. Створіть функцію get_element, яка приймає список lst та індекс idx і повертає елемент зі списку за вказаним індексом. 
Додайте декоратор @check_index_error до цієї функції.
"""
@check_index_error
def get_element(lst, idx):
    return lst[idx]

"""
5. Напишіть кілька тестових випадків для кожної з функцій divide та get_element, включаючи ситуації, де можуть виникнути помилки.
6. Перевірте роботу декораторів та функцій, запустивши тести.
7. У випадку виявлення помилок, переконайтеся, що декоратори виводять відповідні повідомлення та завершають виконання програми.
"""
def test_divide():
    print("divide(10, 2) =", divide(10, 2))
    print("divide(9, 3) =", divide(9, 3))

    # Помилковий тест:
    print("divide(5, 0) =", divide(5, 0))


def test_get_element():
    numbers = [10, 20, 30, 40]

    print("get_element(numbers, 0) =", get_element(numbers, 0))
    print("get_element(numbers, 2) =", get_element(numbers, 2))

    # Помилковий тест:
    print(
        "get_element(numbers, 10) =",
        get_element(numbers, 10)
    )


if __name__ == "__main__":
    test_divide()
    test_get_element()