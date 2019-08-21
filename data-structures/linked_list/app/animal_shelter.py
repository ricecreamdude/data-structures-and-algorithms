from linked_list import LinkedList
from linked_list import Node

class Dog(Node):
  def __init__(self):
    self.value = "dog"
    self.next = None

class Cat(Node):
  def __init__(self):
    self.value = "cat"
    self.next = None

class AnimalShelter(LinkedList):

  def __init__(self):  
    self.head = None
  
  def enqueue(self, animalNode):
    """
    Inputs (AnimalNode)
    Creates a new node and inserts into onto the end of the queue
    returns nothing
    """

    #Empty queue
    if self.head == None:
      self.head = animalNode
      return 

    #Values exist in queue
    current = self.head

    #Traverse the list
    while current:
      if current.next == None:
        current.next = animalNode
        return
      
      current = current.next

  def pref_dequeue(self, pref=None):
    """
    Input string "cat" or "dog" in order to filter through the queue and remove the first instance of preferred
    node

    Returns removed node
    If no preference given, returns None
    """
    current = self.head
    previous = None 


    if pref is None:
      return None

    while current:
      if current.value == pref:

        self.head = previous or current.next

        return current     
        
      prev = current
      current = current.next    

    return "pref_dequeue Error: Please enter 'cat' or 'dog'. "
    #Check to see if the current node 




if __name__ == '__main__':
  assert LinkedList