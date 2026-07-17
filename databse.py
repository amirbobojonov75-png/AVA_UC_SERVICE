import sqlite3


def connect():
    return sqlite3.connect("database.db")


def create_tables():
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        uc TEXT,
        price TEXT,
        pubg_id TEXT,
        status TEXT
    )
    """)

    db.commit()
    db.close()