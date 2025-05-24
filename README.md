#  AutoInsight – Email-Driven Data Extraction & Dashboard

AutoInsight is an end-to-end automation tool built with Python and Flask, designed to **read structured data from emails**, **store it into a database**, and **visualize it on a dynamic web dashboard**. Perfect for teams that rely on daily reports or structured updates via email but want to ditch manual processing and embrace automation.

---

## Features

- **Automated Email Parsing**  
  Connects to a mailbox and fetches emails with specific patterns/subjects.

- **Smart Data Extraction**  
  Parses structured content (CSV, tabular text, etc.) from email bodies or attachments.

- **Database Storage**  
  Stores parsed data into a relational database (SQLite/MySQL/PostgreSQL – configurable).

- **Web-Based Dashboard**  
  Flask-powered dashboard to visualize key metrics, search records, and filter insights.

- **Scheduled Jobs (Optional)**  
  Use cron or Celery for scheduled email reads and data refresh.

---

## Tech Stack

| Layer           | Tech Used                     |
|----------------|-------------------------------|
| Backend         | Python 3.x, Flask             |
| Email Handling  | `imaplib`, `email`, `re`, etc.|
| Parsing         | Custom parser / Pandas        |
| Database        | SQLite (default), SQLAlchemy ORM |
| Frontend        | HTML, CSS, Jinja2, Bootstrap  |
| Deployment      | Gunicorn, Nginx (Optional)    |

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SrikarPadakanti/AutoInsight.git
cd autoinsight
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Email and DB
Update config.py with:

- Your email credentials (use an app password, not your real one!)

- Email subject pattern/filters

- Database URI

### 5. Run the App

```bash
python main.py
```
Then open your browser and head to Flask URL

---

## Sample Use Cases
- Automate parsing of daily sales/finance reports

- Pull ticket updates or client reports directly from emails

- Centralize scattered data from multiple mail threads

---

## Security Notes
- Use environment variables or secrets manager in production

- Never hardcode credentials (especially not in public repos)
