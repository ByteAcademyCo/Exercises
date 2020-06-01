 # Queue elements after sortedIndex are  
# already sorted. This function returns  
# index of minimum element from front to  
# sorted_ndex  
def min(q, sorted_index): 
    min_index = -1
    min_val = 999999999999
    n = q.qsize() 
    for i in range(n): 
        curr = q.queue[0]  
        q.get()
  
        # we add the condition i <= sorted_index  
        # because we don't want to traverse  
        # on the sorted part of the queue,  
        # which is the right part.  
        if (curr <= min_val and i <= sorted_index): 
            min_index = i  
            min_val = curr 
        q.put(curr) 
    return min_index 
  
# Moves given minimum element to  
# rear of queue  
def mintorear(q, min_index): 
    min_val = None
    n = q.qsize() 
    for i in range(n): 
        curr = q.queue[0]  
        q.get() 
        if (i != min_index):  
            q.put(curr)  
        else: 
            min_val = curr 
    q.put(min_val) 
  
def sort(q): 
    for i in range(1, q.qsize() + 1): 
        min_index = min(q, q.qsize() - i)  
        mintorear(q, min_index) 
  
if __name__ == '__main__': 
    from queue import Queue 
    q = Queue() 
    q.put(20)  
    q.put(11)  
    q.put(51)  
    q.put(7)  
      
    # Sort queue  
    sort(q)  
      
    # Presorted queue  
    while (q.empty() == False): 
        print(q.queue[0], end = " ")  
        q.get() 