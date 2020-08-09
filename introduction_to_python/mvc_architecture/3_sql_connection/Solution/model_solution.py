import sqlite3 

DB_name = 'myDB'

def create(db=None):
    if db is None:
        mydb = ':memory:'
        return mydb 
    else:
        mydb = '{}.db'.format(db)
        return db
    connection = sqlite3.connect(db)
    return connection
    
def query(connection, create_table_student):
    c = connection.cursor()
    return c.execute(create_table_student)
