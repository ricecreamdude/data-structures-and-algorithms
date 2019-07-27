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

if __name__ == "__main__":
  print('Hello from Tree')

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

  def contains():
    """
      Accepts a value and returns a boolean indicating 
      whether or not the value is in the tree at least once.
    """
    pass

class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

if "__main__" == __name__:
  bst = BinarySearchTree()

  bst.add(30)
  bst.add(35)
  bst.add(40)
  bst.add(25)
  bst.add(20)
  bst.add(15)
  bst.add(45)
  bst.add(50)



  print( bst.inOrder() )

