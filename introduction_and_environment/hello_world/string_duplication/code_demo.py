#Python3 code to demonstrate 
# String Split including spaces 
# using list comprehension + split() 
  
# initializing string 
test_string = "GfG is Best"
  
# printing original string 
print("The original string : " + str(test_string)) 
  
# using list comprehension + split() 
# String Split including spaces 
res = [i for j in test_string.split() for i in (j, ' ')][:-1] 
  
# print result 
print("The list without omitting spaces : " + str(res)) 