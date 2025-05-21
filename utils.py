# utils.py
import sqlite3
from pathlib import Path

DB_PATH = Path("data/autoinsight.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # to get dict-like cursor
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create a sample table for parsed data (you'll expand this)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            received_date TEXT,
            extracted_info TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_email_data(sender, subject, received_date, extracted_info):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO email_data (sender, subject, received_date, extracted_info)
        VALUES (?, ?, ?, ?)
    """, (sender, subject, received_date, extracted_info))
    conn.commit()
    conn.close()