# Code your solution here
month = input('Enter any month:')
month_dict = {'january':'31', 'february':'28, 29', 'march':'31', 'april':'30', 'may':'31', 'june':'30', 'july':'31', 'august':'31','september':'30', 'october':'31', 'november':'30', 'december':'31'}
def data(month):
    if month in month_dict.keys():
        return month_dict[month]
    else:
        return None
        
print(data(month))