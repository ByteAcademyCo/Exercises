import sqlite3

class Listing:

    tablename = "listings"
    dbpath = "..data/listings.db"

    def __init__(self, name, quantity, price, location, pk=None):
        self.pk = pk
        self.name = name
        self.quantity = quantity
        self.price = price
        self.location = location


    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO listing VALUES(name, quantity, price, location)")
            

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE listing SET name = self.name WHERE pk = self.pk""")
            

    def delete(self):
        pass


    @classmethod
    def select_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            # TODO: prevent sql injection
            sql = f"""SELECT * from {cls.tablename}"""
            cursor.execute(sql)
            return cursor.fetchall()


    @classmethod
    def select_one(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            # TODO: prevent sql injection
            sql = f"""SELECT * from {cls.tablename}"""
            cursor.execute(sql)
            return cursor.fetchone()


if __name__ == "__main__":
    listings = Listing.select_all()
    print(listings)
    new_item = Listing("name", 5, 12.99, "test location")
    new_item.insert()