# Tree

* You are provided with the basic code for a Binary Search Tree (BST) with \_\_init\_\_, and insert already implemented. Your goal is to implement the methods listed below in the specified runtime. Tests are provided for each implementation 
  * Implement \_\_len\_\_ in O(n) runtime
  * Implement search in O(logn) and traverse in O(n) runtime
  * Implement \_\_len\_\_ in O(1) runtime.
    * Hint: Need to modify \_\_init\_\_ and possibly other methods as well

```Python
class Node:
  def __init__(self, num, left = None, right = None):
    self.num = num
    self.left = left
    self.right = right
    
  def __lt__(self, other):
    return self.num < other.num
    
  def __len__(self):
    pass
    
  def insert(self, num):
    new_node = Node(num)
    if new_node < self:
      if self.left == None:
        self.left = new_node
      else:
        self.left.insert(num)
    else:
      if self.right == None:
        self.right = new_node
      else:
        self.right.insert(num)
        
  def traverse(self, num):
    pass
  def search(self, num):
    pass
```

* Initialization
```Python
t = Node(10,
         Node(5,
              Node(0,
                   None,
                   Node(2, None, None)),
              Node(8,
                   None,
                   None)),
         Node(20,
              Node(15,
                   None,
                   None),
              Node(30,
                   None,
                   Node(70,
                        None,
                        None))))             

```

* Length
```Python
len(t) == 9
```

* Search - return True if num exists, False otherwise
```Python
t.search(40) == False
t.search(70) == True
```

* Traverse - return a list of all the numbers in sorted order
```Python
t.traverse() == [0, 5, 8, 10, 15, 20, 30, 70]
```


