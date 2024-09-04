import sqlite3

def create_database():
    conn = sqlite3.connect('cattle_diseases.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS cattle_diseases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cattle_id TEXT,
            age INTEGER,
            breed TEXT,
            weight REAL,
            symptoms TEXT,
            diagnosis TEXT,
            treatment TEXT,
            date_of_entry DATE
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
