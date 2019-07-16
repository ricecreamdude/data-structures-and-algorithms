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


  def __str__(self, node, str=''):

    if(node.next):
      if(node == self.head):
        str += "The list contains "
      str += f"{node.value}, "
      return self.__str__(node.next, str) 
    if(node.next == None):
      str += f"and {node.value}."
      return str

  def kthFromEnd(self, k):

    length = 0
    current = self.head
    foundEnd = False

    if k < 0:
      return 'Cannot search for a negative number.'

    ## returns the length of the list
    while foundEnd == False:
      length += 1
      if  current.next == None:
        foundEnd = True
        break
      current = current.next

    if length < k:
      return 'Too long'

    if length == 1 and current.next == None:
      return current.value

    diffCounter = 0
    diff = length - k
    current = self.head

    while diffCounter < diff:
      diffCounter += 1
      current = current.next

    return current.value

class Node():

  def __init__(self, value, next=None):
    self.test = 'test'
    self.value = value
    self.next = next

  # return 'Node'