import pytest
from left_join import leftJoin
from hash_table import HashTable


def test_left_join_init():
  assert leftJoin


def test_left_join_returns_left_join():

  right = HashTable()
  left = HashTable()

  keysList = ['ascend', 'lift', 'jump', 'offer', 'hot', 'cold']

  right.add('ascend','rise')
  right.add('lift','hoist')
  right.add('jump','hop')
  right.add('offer','suggest')

  left.add('ascend','descend')
  left.add('lift','drop')
  left.add('hot','cold')
  left.add('sad','glee')

  leftJoin(left, right, keysList)

  assert right