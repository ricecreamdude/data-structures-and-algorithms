from .stack.stack import Stack

class Stack:
  def __init__(self):
    self.head = None

  def pop(self):

    if self.head:
      popped = self.head
      self.head = self.head.next

      return popped

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