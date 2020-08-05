# Write your solution here
class MyString():
    def __init__(self):
        self.input_string = None
    def set_string(self, input_string):
        self.input_string = input_string
    def upper_string(self):
        if self.input_string == None:
            return 'undefined'
        else:
            return self.input_string.upper()