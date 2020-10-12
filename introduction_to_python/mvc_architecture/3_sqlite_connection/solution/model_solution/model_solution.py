import sqlite3


def create():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    query = (
        "CREATE TABLE IF NOT EXISTS student(student_id integer , student_name text);"
    )
    cursor.execute(query)
    return


def query():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    query = "INSERT INTO student VALUES(1,'abc');"
    cursor.execute(query)
    query = "INSERT INTO student VALUES(2,'xyz');"
    cursor.execute(query)
    query = "SELECT * FROM student;"
    cursor.execute(query)
    data = cursor.fetchall()
    # connection.commit()
    # connection.close()
    return data
