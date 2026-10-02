import sqlite3


DB_NAME = "olx_products.db"


def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price INTEGER,
            location TEXT,
            date TEXT,
            url TEXT UNIQUE
        )
    """)

    connection.commit()
    connection.close()


def save_product(title, price, location, date, url):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO products (title, price, location, date, url)
        VALUES (?, ?, ?, ?, ?)
    """, (title, price, location, date, url))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM products
    """)

    products = cursor.fetchall()

    connection.close()

    return products
