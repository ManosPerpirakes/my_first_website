import sqlite3
from time import time, ctime

conn = sqlite3.connect("Database.db")
cursor = conn.cursor()
def set_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS time(
            time CHARVAR
        )
    ''')
    conn.commit()
    cursor.execute("INSERT INTO time (time) VALUES ('" + ctime(time()) + "')")
    conn.commit()

def get_data():
    global timevar
    cursor.execute('''
    SELECT time FROM time
    ''')
    return cursor.fetchall()