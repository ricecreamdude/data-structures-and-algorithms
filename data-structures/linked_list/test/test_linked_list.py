from app.linked_list import *

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

  assert ll.__str__() == response   


##########################################
#                                        #
#             Insertion Tests            #
#                                        #
##########################################


# Can successfully add a node to the end of the linked list

def test_append_init():

  ll = LinkedList()
  assert ll.append

def test_append_adds_single_node():

  ll = LinkedList()
  
  ll.insertNode('apple')
  ll.append('zebra')

  assert ll.__str__() == 'The list contains apple, and zebra.'

# Can successfully add multiple nodes to the end of a linked list
# def test_append_adds_many_nodes():
def test_append_adds_many_nodes():

  ll = LinkedList()

  ll.append('apple')
  ll.append('buffalo')
  ll.append('cat') 
  ll.append('dog')

  actual = ll.__str__()
  expected = 'The list contains apple, buffalo, cat, and dog.'
  assert actual == expected


# Can successfully insert a node before a node located i the middle of a linked list
def test_insert_before_init():
  ll = LinkedList()
  assert ll.insertBefore

def test_insert_node_before_middle():
  ll = LinkedList()

  ll.insertNode('apple')
  ll.append('buffalo')
  ll.append('cat') 

  ll.insertBefore('dog', 'cat')

  assert   ll.__str__() == 'The list contains apple, buffalo, dog, and cat.'

# def test_insert_node_not_found():

# Can successfully insert a node before the first node of a linked list
def test_insert_node_before_first_node():
  ll = LinkedList()

  ll.append('apple')

  ll.insertBefore('dog', 'apple')

  assert ll.__str__() == 'The list contains dog, and apple.'
# Can successfully insert after a node in the middle of the linked list
def test_insert_after_init():
  ll = LinkedList()
  assert ll.insertAfter

def test_insert_node_after_i():
  ll = LinkedList()

  ll.append('apple')
  ll.append('buffalo')
  ll.append('cat') 
  ll.append('dog')

  ll.insertAfter('elephant', 'cat')

  assert ll.__str__() == 'The list contains apple, buffalo, cat, elephant, and dog.' 
  
# Can successfully insert a node after the last node of the linked list

def test_insert_node_at_end():
  ll = LinkedList()

  ll.append('apple')
  ll.append('buffalo')
  ll.append('cat') 
  ll.append('dog')

  ll.insertAfter('elephant', 'dog')

  assert ll.__str__() == 'The list contains apple, buffalo, cat, dog, and elephant.' 