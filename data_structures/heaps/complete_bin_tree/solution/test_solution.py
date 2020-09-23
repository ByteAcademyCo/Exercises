def test_solution():
  from solution import Tree, TreeNode, is_complete

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

  p1 = TreeNode(1)
  p3 = TreeNode(3, None, p1)
  tree4 = Tree(p3)

  tree3 = Tree()
  assert is_complete(tree1) == True
  assert is_complete(tree2) == True
  assert is_complete(tree3) == True
  assert is_complete(tree4) == False