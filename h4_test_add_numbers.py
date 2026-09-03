"""
1. Створіть файл test_add_numbers.py.
2. В цьому файлі напишіть тестовий випадок, який перевіряє правильність роботи функції add_numbers.
"""

import pytest

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    # Перевірка додавання додатних чисел
    assert add_numbers(3, 5) == 8

    # Перевірка додавання від'ємних чисел
    assert add_numbers(-2, -3) == -5

    # Перевірка додавання додатнього та від'ємного чисел
    assert add_numbers(5, -3) == 2

    # Перевірка додавання нуля
    assert add_numbers(0, 7) == 7

    # Перевірка додавання до нуля
    assert add_numbers(10, 0) == 10

if __name__ == "__main__":
    test_add_numbers()
    print("Всі тести пройдено успішно!")

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-2, -3, -5),
    (5, -3, 2),
    (0, 7, 7),
    (10, 0, 10),
])
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected

"""
3. Зробіть аналогічне тестування, але для отримання запиту з інтернету
(запитуємо погоду з openweathermap.com )
"""

import requests

API_KEY = "734dbc125f10e1e7dcce6270230b2864"

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    return response


def test_get_weather():
    response = get_weather("Kyiv")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Kyiv"
    assert "main" in data
    assert "temp" in data["main"]
    assert "weather" in data

