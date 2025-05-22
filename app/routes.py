from flask import Blueprint, render_template
import sqlite3

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    conn = sqlite3.connect('data/autoinsight.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM email_data")
    rows = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', rows=rows)