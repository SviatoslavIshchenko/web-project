"""
Назва завдання: Пошук простих чисел
Опис: Створіть програму, яка шукає всі прості числа в заданому діапазоні. Ви реалізуєте два варіанти пошуку -
один використовуючи один потік, а інший використовуючи багатопоточність.
Кроки:
"""

"""
1. Напишіть функцію is_prime(n), яка приймає число n та повертає True, якщо воно є простим, та False в іншому випадку.
"""
import threading
import time


def is_prime(n):
    """
    Повертає True, якщо число n просте.
    Інакше повертає False.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False

        divisor += 2

    return True


"""
2. Напишіть функцію find_primes_single_thread(start, end), яка знаходить всі прості числа у діапазоні від start до end за допомогою одного потоку.
"""
def find_primes_single_thread(start, end):
    """
    Пошук простих чисел у одному потоці.
    """
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes

"""
3. Напишіть функцію find_primes_multi_thread(start, end), яка робить те ж саме, але використовуючи багатопоточність. 
Розділіть діапазон на дві частини та обчисліть прості числа паралельно в двох потоках. Потім об'єднайте результати.
"""
def find_primes_in_range(start, end, result):
    """
    Допоміжна функція для одного потоку.
    Записує знайдені прості числа у result.
    """
    local_primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            local_primes.append(number)

    result.extend(local_primes)


def find_primes_multi_thread(start, end):
    """
    Пошук простих чисел у двох потоках.
    """
    middle = (start + end) // 2

    result1 = []
    result2 = []

    thread1 = threading.Thread(
        target=find_primes_in_range,
        args=(start, middle, result1)
    )

    thread2 = threading.Thread(
        target=find_primes_in_range,
        args=(middle + 1, end, result2)
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    return result1 + result2

"""
4. Створіть тестові випадки для обох функцій та перевірте, чи вони повертають однаковий результат.
"""
def test_functions():
    """
    Перевіряємо, що обидві функції дають однаковий результат.
    """
    test_cases = [
        (1, 10),
        (1, 100),
        (100, 1000),
        (1000, 5000),
    ]

    for start, end in test_cases:
        single_result = find_primes_single_thread(start, end)
        multi_result = find_primes_multi_thread(start, end)

        print(
            f"Діапазон {start}-{end}:",
            single_result == multi_result
        )

"""
5. Виміряйте час виконання кожної з функцій для різних діапазонів чисел та порівняйте їх ефективність.
"""
def compare_execution_time(start, end):
    """
    Порівнює час виконання обох підходів.
    """
    print(f"\nДіапазон: {start} - {end}")

    start_time = time.perf_counter()

    single_result = find_primes_single_thread(start, end)

    single_time = (time.perf_counter() - start_time)

    start_time = time.perf_counter()

    multi_result = find_primes_multi_thread(start, end)

    multi_time = (time.perf_counter() - start_time)

    print(
        f"Час виконання одним потоком: "
        f"{single_time:.6f} sec"
    )

    print(
        f"Час виконання при використанні багатопоточності: "
        f"{multi_time:.6f} sec"
    )

    print(
        "Результати рівні:",
        single_result == multi_result
    )


if __name__ == "__main__":
    test_functions()

    compare_execution_time(1,10_000)

    compare_execution_time(1,100_000)

    compare_execution_time(1,500_000)

    """
    6. Зробіть аналіз результатів та поясніть, чому один варіант може бути ефективніший за інший в певних умовах.
    
    Обидві реалізації повертають однаковий список простих чисел, що підтверджує правильність багатопоточного варіанта. 
    Під час вимірювання часу багатопоточна реалізація не показала значного прискорення порівняно з однопотоковою, 
    а в деяких випадках виконувалася повільніше. Взагалі кажучи, пошук простих чисел є простою задачею: 
    більша частина часу витрачається безпосередньо на обчислення процесором. 
    Крім того, багатопотоковий варіант має додаткові витрати на створення та керування потоками. 
    Тому багатопоточний варіант більш ефективний, де потоки значну частину часу очікують мережу, файли тощо
    """

