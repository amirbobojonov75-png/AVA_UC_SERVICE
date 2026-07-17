import sqlite3


def add_user(user_id, full_name, username):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (user_id, full_name, username)
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            full_name,
            username
        )
    )

    db.commit()
    db.close()


def add_order(user_id, username, uc, price, pubg_id):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO orders
        (user_id, username, uc, price, pubg_id, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            username,
            uc,
            price,
            pubg_id,
            "Kutilmoqda"
        )
    )

    db.commit()
    db.close()


def get_orders(user_id):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT id, uc, price, pubg_id, status
        FROM orders
        WHERE user_id = ?
        """,
        (user_id,)
    )

    orders = cursor.fetchall()

    db.close()

    return orders