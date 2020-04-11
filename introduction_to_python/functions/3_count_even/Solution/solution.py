# Code your solution here
def count(*l):
    new_l=[]
    for i in l:
        if i%2==0:
            new_l.append(i)
    return new_l
result=count(1,2,4,6,7,98,77,88,44,39,12,11,69,100,99)
print(result)