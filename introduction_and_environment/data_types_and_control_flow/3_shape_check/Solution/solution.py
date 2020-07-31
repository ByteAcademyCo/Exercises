# Code your solution here
figure = input('Enter any geometric shape value:')
my_dict = {'3':'Triangle', '4':'Quadrilateral', '5':'Pentagon', '6':'Hexagon', '7':'Heptagon', '8':'Octagon', '9':'Nonagon'}

def data(figure):
    if figure in my_dict:
        return my_dict[figure]
    else:
        return 'None'
print(data(figure))