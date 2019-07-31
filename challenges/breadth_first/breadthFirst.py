def breadth_tree(tree):
  queue = Queue()

  queue.enqueue(tree.root)

  list = []

  while queue.head:

    tNode = queue.head.value

    list.append(tNode.value)

    if(tNode.left):
      print('left')
      queue.enqueue(tNode.left)
  
    if(tNode.right):
      print('right')
      queue.enqueue(tNode.right)

    queue.dequeue()

  return list

#############################################################
#                                                           #
#              Copied Code from Other Modules               #
#                                                           #
#############################################################

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
    n = treeNode(value)

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

class treeNode():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Queue:
  def __init__(self):
    self.head = None

  def enqueue(self, value):

    newNode = queueNode(value)
    node = self.head

    if node is None:
      self.head = newNode
      return 'new value added to head'

    #Navigate to the end of the queue
    while node.next:
      node = node.next
      
    #Add the new queue node to the end of the queue
    node.next = newNode

    return 'Added node to queue' 

  def dequeue(self):

    #move to last value in the list
    #Remove reference to the last value so it is garbage collected
    
    if self.head:
      current = self.head
      next = None
      
      if current.next:
        next = current.next

      self.head = next

      return current.value
          
    return 'The queue is empty, nothing removed'

  def peek(self):
    if length > 0:
      return self.head.value

class queueNode:
  def __init__(self, value):
    self.value = value
    self.next = None

#######################################
#                                     #
#              Test Code              #
#                                     #
#######################################

if "__main__" == __name__:
  bst = BinarySearchTree()

  one = treeNode('one')
  two = treeNode('two')
  three = treeNode('three')
  four = treeNode('four')
  five = treeNode('five')
  six = treeNode('six')

  one.left = two
  one.right = three
  two.left = four
  two.right = five
  three.right = six

  bst.root = one

  breadth_tree(bst)