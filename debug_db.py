import sqlite3

conn = sqlite3.connect("data/autoinsight.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM email_data")
count = cursor.fetchone()[0]

print(f"🧾 Rows in email_data: {count}")

cursor.execute("SELECT * FROM email_data")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()