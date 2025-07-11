import sqlite3
from datetime import datetime

conn = sqlite3.connect("db/database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    method TEXT,
    reason TEXT,
    photo TEXT,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS settings (
    user_id INTEGER PRIMARY KEY,
    salary REAL,
    code TEXT
)
""")

conn.commit()

def add_transaction(user_id, amount, method, reason, photo):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO transactions (user_id, amount, method, reason, photo, date) VALUES (?, ?, ?, ?, ?, ?)",
                   (user_id, amount, method, reason, photo, now))
    conn.commit()

def get_balance(user_id, method):
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND method = ?", (user_id, method))
    result = cursor.fetchone()[0]
    return result or 0
