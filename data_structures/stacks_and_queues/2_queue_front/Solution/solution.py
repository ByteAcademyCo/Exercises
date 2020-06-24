# Code your solution here
def queue():
    import queue
    queue_a = queue.Queue(maxsize=5)   # Queue is created as an object 'queue_a'
    queue_a.put(99)   
    queue_a.put(66)   
    queue_a.put(77)   # Data is inserted in 'queue_a' at the end using put()  
    queue_a.put(44)
    queue_a.put(11)   
    return queue_a.get() # get() takes data from from the head of the Queue   
result=queue()
print(result)