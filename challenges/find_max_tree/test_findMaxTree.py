from findMaxTree import *

def test_init_findMaxTree():

  assert getMaxValue

def test_findMaxTree_empty():
  bst = BinarySearchTree()

  assert getMaxValue(bst) == 0

def test_getMaxValue():
  bst = BinarySearchTree()

  bst.add(10)
  bst.add(15)
  bst.add(5)
  bst.add(8)
  bst.add(3)
  bst.add(12)
  bst.add(17)

  assert getMaxValue(bst) == 17