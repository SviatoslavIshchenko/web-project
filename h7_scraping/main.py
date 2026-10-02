from database import (
    create_table,
    save_product,
    get_all_products
)
from scraper import get_page, parse_page, parse_card


create_table()

print("Базу даних і таблицю products створено.")

html = get_page()

print("Розмір HTML:", len(html))

cards = parse_page(html)

for card in cards:
    title, price, location, date, link = parse_card(card)

    print("Назва:", title)
    print("Ціна:", price)
    print("Місце:", location)
    print("Дата:", date)
    print("Посилання:", link)
    print("-" * 50)

    save_product(title, price, location, date, link)


products = get_all_products()

print("Кількість товарів у базі:", len(products))