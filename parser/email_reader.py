from imapclient import IMAPClient
import email
from bs4 import BeautifulSoup
import sqlite3
from config.creds import EMAIL_ID, EMAIL_PASSWORD
import os

IMAP_SERVER = "imap.gmail.com"
DB_PATH = "data/autoinsight.db"

def connect_email():
    server = IMAPClient(IMAP_SERVER, ssl=True)
    server.login(EMAIL_ID, EMAIL_PASSWORD)
    server.select_folder("INBOX", readonly=True)
    return server

def fetch_target_emails(server, keyword="Daily Report", limit=5):
    messages = server.search(["SUBJECT", keyword])
    latest_ids = messages[-limit:]
    fetched = server.fetch(latest_ids, ["RFC822"])
    return [fetched[mid][b"RFC822"] for mid in latest_ids]

def parse_email(raw_email):
    msg = email.message_from_bytes(raw_email)
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                html = part.get_payload(decode=True).decode()
                return extract_table_data(html)
    else:
        return []

def extract_table_data(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    if not table:
        print("⚠️  No table found in this email.")
        return None  # or return [] if you prefer

    rows = table.find_all("tr")[1:]  # Skip header
    data = []

    for row in rows:
        cols = row.find_all("td")
        data.append([col.get_text(strip=True) for col in cols])

    return data

def store_to_db(data, table_name="email_data"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            field1 TEXT, field2 TEXT, field3 TEXT
        )
    ''')

    for entry in data:
        if len(entry) >= 3:
            cursor.execute(f'''
                INSERT INTO {table_name} (field1, field2, field3)
                VALUES (?, ?, ?)
            ''', (entry[0], entry[1], entry[2]))

    conn.commit()
    conn.close()