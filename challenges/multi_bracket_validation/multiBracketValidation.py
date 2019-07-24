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
    #LIFO
    newNode = Node(value)
    
    next = self.head
    newNode.next = next 
    self.head = newNode

    return



class MultiBracketValidation(Stack):

  def validate(self, string):
    # list = list(string)
    #Create a node based on inputted string

    #Check for string type, if open bracket
    #
    if string == '[':
      self.push( SquareBracket() )

    if string == '{':
      self.push( CurlyBracket() )

    if string == '(':
      self.push( CircleBracket() )

    return 

  # def insertNode(self, bracket):
    """
    input (bracket)
    Takes in a single string as brack type and returns a bracket objects based on provided string
    return [CircleBracket or SquareBracket or CurlyBracket]
    """
    # return
    
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class CircleBracket:
  def __init__(self):
    self.open = '('
    self.close = ')'

class SquareBracket:
  def __init__(self):
    self.open = '['
    self.close = ']'

class CurlyBracket:
  def __init__(self):
    self.open = '{'
    self.close = '}'





if __name__ == '__main__':
  mbv = MultiBracketValidation()
  mbv.validate('[')
  mbv.validate('(')
  mbv.validate('{')

  print('test:', mbv.peek().open)
  # print('test:', mbv.head.value.open)