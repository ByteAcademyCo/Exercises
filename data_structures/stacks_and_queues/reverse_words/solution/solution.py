class ListNode:
  def __init__(self, value):
      self.value = value
      self.next = None

class Stack:
    def __init__(self):
        self.head_node = None

    def push(self, value):
        new_head = ListNode(value)
        new_head.next = self.head_node
        self.head_node = new_head

    def pop(self):
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.next
            return value
        else:
            raise IndexError
    
    def __bool__(self):
        return not self.head_node == None
    
    def __len__(self):
        cur_node = self.head_node
        num_nodes = 0
        while(cur_node):
            num_nodes += 1
            cur_node = cur_node.next
        return num_nodes

    def __eq__(self, other):
        if(len(self) == len(other)):
            cur_node1 = self.head_node
            cur_node2 = other.head_node
            while(cur_node1):
                if not cur_node1.value == cur_node2.value:
                    return False
                else:
                    cur_node1 = cur_node1.next
                    cur_node2 = cur_node2.next
            return True
        return False


def reverse_words(sentence):
    # create a stack to keep track of our words
    stack = Stack()
    # split our sentence on spaces
    slst = sentence.split()
    # push all words onto our stack. The last word will
    # then be at the top of the stack.
    for word in slst:
        stack.push(word)
    new_s = ""
    # itterate through the stack appending each word to our new sentence
    while stack:
        new_s += stack.pop()
        new_s += " "
    # remove the last space character at the end of the sentence
    return new_s[:-1]

sentence = "hello bonjour aloha"
print(reverse_words(sentence))
    

    
