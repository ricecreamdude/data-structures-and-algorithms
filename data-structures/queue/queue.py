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

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

if __name__ == '__main__':
  print('hello')