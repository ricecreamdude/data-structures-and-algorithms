def fizzBuzzTree(tree):
  def walk(node):
    if node.left:
      walk(node.left)
    node.value = fizzBuzz(node.value)
    if node.right:
      walk(node.right)

  def fizzBuzz(n):
    if n % 3 is 0 and n % 5 is 0:
      return 'FizzBuzz'
    if n % 3 is 0:
      return 'Fizz'
    if n % 5 is 0:
      return 'Buzz'
    return n

  walk(tree.root)

  return tree

#########################################################
#             Copied Code from another module           #
#########################################################

class BinaryTree():

  def __init__(self):
    self.value = 'tree'
    self.root = None

#   Preorder
#   Root, Left, Right
  def preOrder(self):
    """
    Function used to traverse tree and store tree values in order of Root, Left, Right
    
    returns List
    """
    l = []

    def walk(node):
      l.append(node.value)
      if(node.left):
        walk(node.left)
      if(node.right):
        walk(node.right)
    
    walk(self.root)

    return l

# Inorder
# Left, Root, Right
  def inOrder(self):
    """
    Function used to traverse tree and store tree values in order of Root, Left, Right
    
    returns List
    """
    l = []
    def walk(node):
      if(node.left):
        walk(node.left)      
      l.append(node.value)
      if(node.right):
        walk(node.right)
    
    walk(self.root)

    return l

# Postorder
# Left, Right, Root
  def postOrder(self):
    """
    Function used to traverse tree and store tree values in order of Root, Left, Right
    
    returns List
    """
    l = []
    def walk(node):
      if(node.left):
        walk(node.left)      
      if(node.right):
        walk(node.right)
      l.append(node.value)

    walk(self.root)

    return l



class BinarySearchTree(BinaryTree):
  def __init__(self):
    BinaryTree.__init__(self)

  def add(self, value):
    """
      Accepts a value, and adds a new node with that value 
      in the correct location in the binary search tree.
    """
    n = Node(value)

    def walk(node):
      if not self.root:
        self.root = n 
        return

      if n.value > node.value:
        if not node.right:
          node.right = n
          return
        walk(node.right)

      if n.value < node.value:
        if not node.left:
          node.left = n
          return
        walk(node.left)

    walk(self.root)

  def contains(self, value):
    """
      Accepts a value and returns a boolean indicating 
      whether or not the value is in the tree at least once.
    """
    
    def walk(node):
      if value == node.value:
        return True

      if value > node.value:
        if not node.right:
          return False
        return walk(node.right)

      if value < node.value:
        if not node.left:
          return False
        return walk(node.left)

    return walk(self.root)

class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

if "__main__" == __name__:
  bst = BinarySearchTree()

  bst.add(10)
  bst.add(15)
  bst.add(5)
  bst.add(8)
  bst.add(3)
  bst.add(12)
  bst.add(17)

  fizz = fizzBuzzTree(bst)

  print(fizz.inOrder())