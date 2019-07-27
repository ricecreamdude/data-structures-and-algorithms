from tree import Node, BinaryTree, BinarySearchTree


# Can successfully instantiate an empty tree
def test_tree_init():

  t = BinaryTree()

  assert t.value is 'tree'

def test_binary_tree_init():

  bst = BinarySearchTree()

  assert bst

def test_node():

  n = Node('potato')

  assert n.value is 'potato'
  assert n.left is None
  assert n.right is None

# Can successfully instantiate a tree with a single root node
def test_tree_single_root():
 
  bst = BinarySearchTree()

  bst.add(1)

  assert bst.root.value is 1

# Can successfully add a left child and right child to a single root node
def test_tree_left_right():
 
  bst = BinarySearchTree()
  
  bst.add(10)
  bst.add(15)
  bst.add(5)

  bst.add(8)
  bst.add(3)

  bst.add(12)
  bst.add(17)

  assert bst.root.left.value is 5
  assert bst.root.right.value is 15
  assert bst.root.value is 10

# Can successfully return a collection from a preorder traversal

def test_preorder_traversal():

  bst = BinarySearchTree()
  
  bst.add(10)
  bst.add(15)
  bst.add(5)
  bst.add(8)
  bst.add(3)
  bst.add(12)
  bst.add(17)

  l = bst.preOrder()

  assert l == [10, 5, 3, 8, 15, 12, 17]

# Can successfully return a collection from an inorder traversal

def test_inorder_traversal():

  bst = BinarySearchTree()
  
  bst.add(10)
  bst.add(15)
  bst.add(5)
  bst.add(8)
  bst.add(3)
  bst.add(12)
  bst.add(17)

  l = bst.inOrder()

  assert l == [3, 5, 8, 10, 12, 15, 17]
# Can successfully return a collection from a postorder traversal
def test_postorder_traversal():

  bst = BinarySearchTree()
  
  bst.add(10)
  bst.add(15)
  bst.add(5)
  bst.add(8)
  bst.add(3)
  bst.add(12)
  bst.add(17)

  l = bst.postOrder()

  assert l == [3, 8, 5, 12, 17, 15, 10]


def test_contains_bst():

  bst = BinarySearchTree()
  
  bst.add(10)
  bst.add(15)
  bst.add(5)
  bst.add(8)
  bst.add(3)
  bst.add(12)
  bst.add(17)

  assert bst.contains(10) is True
  assert bst.contains(8) is True
  assert bst.contains(3) is True
  assert bst.contains(17) is True
  assert bst.contains(30) is False