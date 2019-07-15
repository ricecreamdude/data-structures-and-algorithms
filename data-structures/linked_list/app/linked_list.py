class Node():

  def __init__(self, value, next=None):
    self.test = 'test'
    self.value = value
    self.next = next
  # return 'Node'

class LinkedList():

  def __init__(self):
    self.head = None
  
  #insert head 
  def insertNode(self, value, next=None):
    self.head = Node(value, self.head)

  def valueExists(self, node, q=None):

    if (q == None):
      return True

    if (q == node.value):
      return True

    if (q != node.value):
      if (node.next == None):
        return False
      node = node.next
      return self.valueExists(node, q)

    else:
      return 'Error with query'


  def __str__(self, node=None, str=''):

    node = node or self.head

    if (node == None):
      return 'This list is empty'

    if(node.next):
      if(node == self.head):
        str += "The list contains "
      str += f"{node.value}, "
      return self.__str__(node.next, str)

    if(node.next == None):
      str += f"and {node.value}."
      return str

  def append(self, newNodeValue, cur=None):

    if self.head == None:
      self.insertNode( newNodeValue ) 
      return

    current = cur or self.head

    if (current.next == None):
      current.next = Node(newNodeValue) 
      return 
    return self.append(newNodeValue, current.next)
