from tree import BinarySearchTree
from hash_table import HashTable

#Split below functions into secitons to allow for testing
def traverseTree(treeNode, callback=None, hashTable=None):
  
  response = []

  #left, current, right
  if treeNode.left:
    traverseTree(treeNode.left, callback, hashTable)

  #If there's a hash table, traverse tree and compare values to hash table values
  if hashTable:
    matchValue = findMatches(treeNode.value, hashTable)
    response.append(matchValue)
  #If the callback is equal to ht.add, fire the callback
  if callback == HashTable.add:
    callback(treeNode.value, treeNode.value)

  if treeNode.right:
    traverseTree(treeNode.right, callback, hashTable)  

  return response

def findMatches(value, hashTable):

  if hashTable.contains( str(value) ) is not None:
    return value    


#Initialize all functionality here
if __name__ == "__main__":

  treeA = BinarySearchTree()
  treeB = BinarySearchTree()

  treeA.add(10)
  treeA.add(5)
  treeA.add(8)
  treeA.add(3)
  treeA.add(13)
  treeA.add(15)

  treeB.add(9)
  treeB.add(5)
  treeB.add(7)
  treeB.add(3)
  treeB.add(14)
  treeB.add(15)

  ht = HashTable()

  treeList = traverseTree(treeA.root, ht.add, None)
  answer = traverseTree(treeB.root, None, ht)

  print(answer)


