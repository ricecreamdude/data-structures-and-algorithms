class Queue:
  def __init__(self):
    self.head = None
    self.length = 0

  def enqueue(self, value):

    if self.head is None:
      self.head = Node(value)
      self.length += 1
      return 'Added node to queue' 

    newNode = Node(value)
    next = self.head.next

    newNode.next = next  
    self.head = newNode

    return 'Added node to queue'

  def dequeue(self):

    #move to last value in the list
    #Remove reference to the last value so it is garbage collected
    endReached = False
    
    if(self.length > 0):
      current = self.head
      next = current.next
      while endReached == False:
        if(next.next == None):
          current.next = None
          endReached == True
          self.length -=1
        current = current.next  
        next = current.next
      return f"Removed node {next} from the queue"
    
    return 'The queue is empty, nothing removed'

  def peek(self):
    if length > 0:
      return self.head.value

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

if __name__ == '__main__':
  print('hello')