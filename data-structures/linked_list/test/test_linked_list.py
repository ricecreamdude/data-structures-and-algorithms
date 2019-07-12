from app.linked_list import LinkedList, Node

#Can successfully instantiate an empty linked list
def test_linked_list_init():  

  assert LinkedList


  

# def test_linked_list_create_node():

# Can properly insert into the linked list

def test_ll_insert():

  ll = LinkedList()
  ll.insertNode('test')
  ll.insertNode('a')
  ll.insertNode('wow')

  assert ll.head.value == 'wow'
  assert ll.head.next.value == 'a'
  assert ll.head.next.next.value == 'test' 
  





def test_node_init():

  assert Node

def test_node_has_given_value():

  newNode = Node('potato')

  assert newNode.value == 'potato'
  assert newNode.next is None


# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list