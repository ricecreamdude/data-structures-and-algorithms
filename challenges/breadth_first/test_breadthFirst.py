from breadthFirst import *

def test_breadth_first_init():
  
  p = breadth_tree

  assert p

def test_breadth_first_tree():

  bst = BinarySearchTree()

  one = treeNode('one')
  two = treeNode('two')
  three = treeNode('three')
  four = treeNode('four')
  five = treeNode('five')
  six = treeNode('six')

  one.left = two
  one.right = three
  two.left = four
  two.right = five
  three.right = six

  bst.root = one

  breadth_tree(bst)

  assert breadth_tree(bst) == ['one','two','three','four','five','six']
