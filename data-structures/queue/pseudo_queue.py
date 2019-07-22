class PseudoQueue:
  def __init__(self):
    self.addStack = Stack()
    self.removeStack = Stack()

  def enqueue(self, value):

    # if self.addStack.peek() == None:
    #   self.switchStack(self.removeStack, self.addStack)
    #   self.addStack.push(value)
    #   return
    #Add to the addstack queue once it's empty
    self.switchStack(self.addStack, self.removeStack)
    self.switchStack(self.removeStack, self.addStack)    
    self.addStack.push(value)

  def dequeue(self):

    self.switchStack(self.removeStack, self.addStack) 
    self.switchStack(self.addStack, self.removeStack)

    node = self.removeStack.pop()

    return node;  

  def switchStack(self, stackWithData, stackToFill):
    if stackWithData.peek() == 'Stack is empty':
      return 
    stackToFill.push( stackWithData.pop() )
    return self.switchStack(stackWithData, stackToFill)

class Stack:
  def __init__(self):
    self.head = None

  def pop(self):

    if self.head:
      popped = self.head
      self.head = self.head.next

      return popped.value

    return 'Stack is empty, no actions taken'

  def peek(self):
    if self.head:
      return self.head.value
    return 'Stack is empty'

  def push(self, value):
    #import Node for this
    newNode = Node(value)

    if self.head is None:
      self.head = newNode
      return 'New head created for list'

    newNode.next = self.head
    self.head = newNode
    return f'Added Node with value {value} to the stack.'

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None