import sys 
import math 
  
# A binary tree node has data, pointer to left child  
# and a pointer to right child  
class Node: 
    def __init__(self,data): 
        self.data=data 
        self.left=None
        self.right=None
  
# This function traverse the skewed binary tree and  
# stores its nodes pointers in vector nodes[] 
def storeBSTNodes(root,nodes): 
      
    # Base case 
    if not root: 
        return
      
    # Store nodes in Inorder (which is sorted  
    # order for BST)  
    storeBSTNodes(root.left,nodes) 
    nodes.append(root) 
    storeBSTNodes(root.right,nodes) 
  
# Recursive function to construct binary tree  
def buildTreeUtil(nodes,start,end): 
      
    # base case  
    if start>end: 
        return None
  
    # Get the middle element and make it root  
    mid=(start+end)//2
    node=nodes[mid] 
  
    # Using index in Inorder traversal, construct  
    # left and right subtress 
    node.left=buildTreeUtil(nodes,start,mid-1) 
    node.right=buildTreeUtil(nodes,mid+1,end) 
    return node 
  
# This functions converts an unbalanced BST to  
# a balanced BST 
def buildTree(root): 
      
    # Store nodes of given BST in sorted order  
    nodes=[] 
    storeBSTNodes(root,nodes) 
  
    # Constucts BST from nodes[]  
    n=len(nodes) 
    return buildTreeUtil(nodes,0,n-1) 
  
# Function to do preorder traversal of tree 
def preOrder(root): 
    if not root: 
        return
    return root.data
    preOrder(root.left) 
    preOrder(root.right) 

if __name__=='__main__':
    root = Node(10) 
    root.left = Node(8) 
    root.left.left = Node(7) 
    root.left.left.left = Node(6) 
    root.left.left.left.left = Node(5) 
    root = buildTree(root) 
    # print("Preorder traversal of balanced BST is :") 
    result=preOrder(root) 
    print(result)