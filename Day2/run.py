import os
from models.listing import Listing

PATH = os.path.dirname(__file__)
Listing.dbpath = os.path.join(PATH, "data", "listings.db")

print(Listing.select_all())
