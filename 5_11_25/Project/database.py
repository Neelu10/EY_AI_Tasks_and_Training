import sqlite3

DB_NAME = "health_data.db"

# Initialize / Create Table
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptoms TEXT,
                duration TEXT,
                severity TEXT,
                diagnosis TEXT,
                diet TEXT,
                report TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# Save Report to DB
def save_report(symptoms, duration, severity, diagnosis, diet, report):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reports (symptoms, duration, severity, diagnosis, diet, report)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (symptoms, duration, severity, diagnosis, diet, report))
        conn.commit()

# Get Reports (Returns List of Dictionaries)
def get_reports():
    conn = sqlite3.connect("health_data.db")
    conn.row_factory = sqlite3.Row   # ✅ Make rows dictionary-like
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return data

