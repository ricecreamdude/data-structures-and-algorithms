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

  def append(self, newNodeValue, cur=None):

    if self.head == None:
      self.insertNode( newNodeValue ) 
      return


    current = cur or self.head

    if (current.next == None):
      current.next = Node(newNodeValue) 
      return 

    return self.append(newNodeValue, current.next)

  def insertBefore(self, newNodeVal, searchVal, curNode=None):

    current = curNode or self.head
    next = current.next

    if current.value == searchVal:
      newNode = Node(newNodeVal)
      newNode.next = self.head
      self.head = newNode
      return

    if next.value == searchVal:
      newNode = Node(newNodeVal)
      current.next = newNode
      newNode.next = next
      return

    return self.insertBefore(newNodeVal, searchVal, next)

  def insertAfter(self, newNodeVal, searchVal, curNode=None):
    
    current = curNode or self.head
    next = current.next or None

    if searchVal == current.value:
      newNode = Node(newNodeVal)
      current.next = newNode
      newNode.next = next
      return
  
    return self.insertAfter(newNodeVal, searchVal, next)



#Testing area
if __name__ == "__main__":
    ll = LinkedList()

    ll.append('apple')
    ll.append('buffalo')
    ll.append('cat')
 

    ll.insertBefore('dog', 'buffalo')

