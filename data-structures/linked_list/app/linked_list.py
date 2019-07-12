class LinkedList():

  def __init__(self):
    self.head = None
  
  #insert head 
  def insertNode(self, value, next=None):
    self.head = Node(value, self.head)


  # return 'linkedList'


class Node():

  def __init__(self, value, next=None):
    self.test = 'test'
    self.value = value
    self.next = next

  # return 'Node'