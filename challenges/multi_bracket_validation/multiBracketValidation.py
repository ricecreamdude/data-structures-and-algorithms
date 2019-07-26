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
    newNode = Node(value)
    next = self.head
    newNode.next = next 
    self.head = newNode
    return


class MultiBracketValidation(Stack):

  def __init__(self):
    self.expected = None
    self.head = None

  def validate(self, string):
    """
    Input: String 
    This method takes in a string and validates it against the bracket criteria detailed in the readme.
    If the provided string leaves the validator with an empty stack, return True.
    All else returns false.

    Output: True, False
    """
    charList = list(string)

    for c in charList:
    #Opening brackets - Adding nodes to the stack
      if c == '[':
        self.push(SquareBracket())
        continue
      if c == '{':
        self.push(CurlyBracket())
        continue
      if c == '(':
        self.push(CircleBracket())
        continue

      #Closing brackets - removing nodes from stack
      if self.head:
        if c == self.head.value.close:
          self.pop()
          continue

        if c != self.head.value.close:
          return False
          break
      else: 
        return False
        break
    #Head must be empty in order for algorithm to complete correctly
    if self.head == None:
      return True

    #Program defaults to FALSE if provided string does not match the method criteria
    print('Head is not empty')
    return False

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
  print('test one:', mbv.validate('[][][]') )
  print('test two:', mbv.validate('[](){}') )
  print('test three:', mbv.validate('[[]{{[[]}}]') )

##########################
#     In class demo:     #
##########################
closers = {
  ')':'('
}

#string = 'string'
#print(string[2])
# => 'r'

openers = ['{', '(', '[']

check_brackets(txt):
  stack = Stack()

  for char in txt:
    if char in openers:
      stack.push(char)
      continue
    if char in closers:
      if stack.peek() != closers[char]:
        return False
      stack.pop()

  return stack.is_empty()


