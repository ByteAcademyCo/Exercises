class MyString():
    def __init__(self):
        self.string = None

    def set_string(self, string):
        self.string = string
    
    def upper_string(self):
        if self.string == None:
            return "undefined"
        else:
            return self.string.upper()
