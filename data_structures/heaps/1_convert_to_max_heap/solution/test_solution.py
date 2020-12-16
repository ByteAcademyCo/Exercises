def test_solution():
  from solution import Tree, TreeNode, MaxHeap, convert_to_maxHeap

  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3, n1, n2)
  n4 = TreeNode(4)
  n5 = TreeNode(5)
  n6 = TreeNode(6, n4, n5)
  n7 = TreeNode(7, n3, n6)
  tree1 = Tree(n7)


  m1 = TreeNode(1)
  m3 = TreeNode(3, m1, None)
  tree2 = Tree(m3)

  tree3 = Tree()
  assert convert_to_maxHeap(tree1)._heap == [7, 6, 5, 2, 3, 1, 4]
  assert convert_to_maxHeap(tree2)._heap == [3, 1]
  assert convert_to_maxHeap(tree3)._heap == []