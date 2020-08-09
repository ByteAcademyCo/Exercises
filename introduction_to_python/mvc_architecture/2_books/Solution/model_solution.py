import json 
book_author_list={"books":{"A Tale of Two Cities":'Charles Dickens',"Lord Of The Rings":'J.R.R. Tolkien',"Dark Psychology":'Steven Turner',"Rich Dad Poor Dad":'Robert T Kiyosaki'}}
book_list = json.dumps(book_author_list)
# json.dumps() is a method in which it turns a python object into a JSON string
def get_list():
    return str(book_list)

def retrive_book(book):
    x = json.loads(book_list)
    books = x['books']
    result = books.get(book)
    return result 
# json.loads() is a method in which it parses a JSON string