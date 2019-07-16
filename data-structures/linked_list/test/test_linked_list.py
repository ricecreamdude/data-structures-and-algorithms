from app.linked_list import LinkedList, Node

#Can successfully instantiate an empty linked list
def test_linked_list_init():  
  assert LinkedList

# Can properly insert into the linked list
# Can properly insert multiple nodes into the linked list
def test_ll_insert_three_nodes():

  ll = LinkedList()
  ll.insertNode('test')
  ll.insertNode('a')
  ll.insertNode('wow')

  assert ll.head.value == 'wow'
  assert ll.head.next.value == 'a'
  assert ll.head.next.next.value == 'test' 
  assert ll.head.next.next.next is None

# Will return true when finding a value within the linked list that exists
# def test_ll_return_value_exists():

#   ll = LinkedList()

#   ll.insertNode('SestTtring')
#   ll.insertNode('testString')
#   ll.insertNode('stringTest')
#   ll.insertNode('gnirtStset')

#   assert ll.valueExists('testString') is True

def test_value_exists_returns_true_for_null():

  ll = LinkedList()

  ll.insertNode('stringTest')

  assert ll.valueExists(ll.head) is True

# Will return false when searching for a value in the linked list that does not exist
def test_value_exists_returns_true_for_match():

  ll = LinkedList()

  ll.insertNode('stringTest')
  ll.insertNode('stringaTest2')
  ll.insertNode('stri2ngTest3')
  ll.insertNode('strin5dgTest5')

  assert ll.valueExists(ll.head, 'stringTest') == True

def test_value_exists_no_match_returns_false():
  ll = LinkedList()

  ll.insertNode('SestTtring')
  ll.insertNode('testString')
  ll.insertNode('stringTest')
  ll.insertNode('gnirtStset')

  assert ll.valueExists(ll.head, 'potato') is False

def test_node_init():

  assert Node

def test_node_has_given_value():

  newNode = Node('potato')

  assert newNode.value == 'potato'
  assert newNode.next is None

# Can properly return a collection of all the values that exist in the linked list
def test_ll_return_all_strings():

  ll = LinkedList()

  response = "The list contains My Hero Academia, Black Mirror, and Game of Thrones."

  ll.insertNode('Game of Thrones')
  ll.insertNode('Black Mirror')
  ll.insertNode('My Hero Academia')

  assert ll.__str__(ll.head) == response   


# Unit Tests

def test_kth_from_end_init():

  ll = LinkedList()
  
  assert ll.kthFromEnd

def test_kth_from_end_return_length():

  ll = LinkedList()

  ll.insertNode('Game of Thrones')
  ll.insertNode('Black Mirror')
  ll.insertNode('My Hero Academia')  
  ll.insertNode('Demon Slayer')
  ll.insertNode('Stranger Things')
  ll.insertNode('YouTube')  

  assert ll.kthFromEnd(3) == "My Hero Academia"
# Where k is greater than the length of the linked list
def test_kth_from_end_k_longer_than_list():

  ll = LinkedList()

  ll.insertNode('Game of Thrones')
  ll.insertNode('Black Mirror')
  ll.insertNode('My Hero Academia')  
  ll.insertNode('Demon Slayer')
  ll.insertNode('Stranger Things')
  ll.insertNode('YouTube')  

  assert ll.kthFromEnd(7) == "Too long"

# Where k and the length of the list are the same
def test_kth_from_end_k_same_length_as_list():

  ll = LinkedList()

  ll.insertNode('Game of Thrones')
  ll.insertNode('Black Mirror')
  ll.insertNode('My Hero Academia')  
  ll.insertNode('Demon Slayer')
  ll.insertNode('Stranger Things')
  ll.insertNode('YouTube')  

  assert ll.kthFromEnd(6) == "YouTube"

# Where k is not a positive integer
def test_kth_from_end_k_same_length_as_list():

  ll = LinkedList()

  ll.insertNode('Game of Thrones')
  ll.insertNode('Black Mirror')
  ll.insertNode('My Hero Academia')  
  ll.insertNode('Demon Slayer')
  ll.insertNode('Stranger Things')
  ll.insertNode('YouTube')  

  assert ll.kthFromEnd(-1) == 'Cannot search for a negative number.'

# Where the linked list is of a size 1

def test_kth_from_end_list_length_one():

  ll = LinkedList()

  ll.insertNode('Game of Thrones')

  assert ll.kthFromEnd(0) == 'Game of Thrones'


# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list