import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "listings.db")
# print(DATAPATH)

def schema(dbpath=DATAPATH):
    # with calls an object's __enter__ method
    # then calls the object's __exit__ method upon
    # exiting the with's block of code OR encountering an exception
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS listings(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            price FLOAT,
            quantity INTEGER,
            location VARCHAR
        );"""
        cursor.execute(sql)

if __name__ == "__main__":
    schema()