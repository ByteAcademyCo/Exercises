# Code your solution here
def queue():
    import queue
    queue_a = queue.Queue(maxsize=5)   # Queue is created as an object 'queue_a'
    queue_a.put(9)   
    queue_a.put(6)   
    queue_a.put(7)   # Data is inserted in 'queue_a' at the end using put()  
    queue_a.put(4)
    queue_a.put(1)   
    return queue_a
data=queue()
result=list(data.queue)
print(result)