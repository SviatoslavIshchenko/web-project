from bs4 import BeautifulSoup
from datetime import datetime

MONTHS = {
    "січня": 1,
    "лютого": 2,
    "березня": 3,
    "квітня": 4,
    "травня": 5,
    "червня": 6,
    "липня": 7,
    "серпня": 8,
    "вересня": 9,
    "жовтня": 10,
    "листопада": 11,
    "грудня": 12,
}

def get_page():
    with open("olx_iphone.html", "r", encoding="utf-8") as file:
        html = file.read()

    return html

def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.find_all("div", attrs={"data-cy": "l-card"})

    print("Знайдено карток:", len(cards))

    return cards

def clean_price(price_text):
    digits = ""

    for char in price_text:
        if char.isdigit():
            digits += char

    if digits:
        return int(digits)

    return None


def parse_card(card):
    image = card.find("img")
    title = image.get("alt")
    title = clean_title(title)

    paragraphs = card.find_all("p")

    price_text = paragraphs[0].get_text(strip=True)
    price = clean_price(price_text)

    location_date = paragraphs[1].get_text(strip=True)
    location, date = location_date.rsplit(" - ", 1)

    location = clean_location(location)
    date = clean_date(date)

    link_tag = card.find("a")
    link = "https://www.olx.ua" + link_tag.get("href")

    return title, price, location, date, link

def clean_date(date_text):
    date_text = date_text.strip()

    if date_text.startswith("Сьогодні"):
        parts = date_text.split()

        time_text = parts[2]
        hour, minute = time_text.split(":")

        now = datetime.now()

        dt = datetime(
            now.year,
            now.month,
            now.day,
            int(hour),
            int(minute)
        )

    else:
        parts = date_text.split()

        day = int(parts[0])
        month = MONTHS[parts[1]]
        year = int(parts[2])

        dt = datetime(year, month, day)

    return dt.strftime("%Y-%m-%d %H:%M:%S")

def clean_location(location_text):
    parts = location_text.split(",")

    parts = [part.strip() for part in parts]

    return ", ".join(parts)

def clean_title(title_text):
    if not title_text:
        return None

    return " ".join(title_text.split())