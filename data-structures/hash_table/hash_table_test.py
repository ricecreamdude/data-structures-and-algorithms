"""
Successfully hash a key to an in-range value
"""
import pytest
from hash_table import HashTable

def test_hash_table_init():
  assert HashTable()

def test_hash_table_is_consistant():
  ht = HashTable()

  test = ht.hash('potato')

  assert ht.hash('potato') == test

#Adding a key/value to your hashtable results in the value being in the data structure
def test_hash_table_add():
 
  ht = HashTable()

  ht.add('Potato', 'fries')

  #Rewriting hashing algorithm here in order to repeat
  testHash = sum( [ord(char) for char in 'Potato'] ) * 599 % 1024

  assert ht.buckets[testHash].head.value['value'] == 'fries'

# Successfully hash a key to an in-range value
def test_hash_in_range():
    ht = HashTable()
    assert  0 <= ht.hash('New York is the largest city in the United States by population') < len(ht.buckets)

# Retrieving based on a key returns the value stored
def test_hash_table_get_stored_value():

  ht = HashTable()

  ht.add('potato', 'fries')

  testValue = ht.get('potato')

  assert testValue == 'fries'

# Successfully retrieve a value from a bucket within the hashtable that has a collision
# Successfully handle a collision within the hashtable
def test_hash_table_get_stored_value_with_same_hash():

  ht = HashTable()

  ht.add('pot', 'fries')
  ht.add('top', 'jakarta')

  assert ht.get('pot') == 'fries'
  assert ht.get('top') == 'jakarta'


# -Successfully returns NONE for a key that does not exist in the hashtable
def test_hash_table_get_DNE_returns_none():

  ht = HashTable()

  testValue = ht.get('lasagna')

  assert testValue == None
