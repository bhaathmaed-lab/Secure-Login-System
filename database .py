import sqlite3

DATABASE = "users.db"

# Create database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create users table
def create_table():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Add new user
def add_user(username, email, password):
    conn = get_db_connection()

    try:
        conn.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, password)
        )
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


# Find user by email
def get_user_by_email(email):
    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    conn.close()

    return user
What this file does:
✅ Creates SQLite database (users.db)
✅ Creates users table
✅ Stores username, email, hashed password
✅ Prevents duplicate email/username
✅ Uses parameterized SQL queries (prevents SQL injection)
Your app.py will import it like:
from database import create_table, add_user, get_user_by_email
Then initialize database:
create_table()