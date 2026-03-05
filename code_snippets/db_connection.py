"""
Database Connection using SQLite
"""

import sqlite3


def connect_database(db_name="college.db"):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print("Database connected successfully")
        return conn, cursor
    except sqlite3.Error as e:
        print("Connection failed:", e)
        return None, None


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        )
    """)


def insert_student(cursor, name, department):
    cursor.execute("INSERT INTO students (name, department) VALUES (?, ?)",
                   (name, department))


def fetch_students(cursor):
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def close_connection(conn):
    if conn:
        conn.commit()
        conn.close()
        print("Connection closed")

if __name__ == "__main__":
    conn, cursor = connect_database()
    if cursor:
        create_table(cursor)
        insert_student(cursor, "John", "CSE")
        print(fetch_students(cursor))
        close_connection(conn)
