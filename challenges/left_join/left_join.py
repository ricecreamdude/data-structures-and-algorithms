from hash_table import HashTable

def leftJoin(htLeft, htRight, keysList):
  answer = []
  i = 0

  while i < len(keysList):
    key = keysList[i]
    print('KEYYYYYYYY', key)
    leftVal = None
    rightVal = None

    if htLeft.get(key) is not None:
      
      leftVal = htLeft.get( keysList[i] ) 
      
      # if htRight.get(key) is not None:
      #   rightVal = htRight.get(key)

      answer.append( [key, leftVal, rightVal] )

    i += 1 

  return answer

if __name__ == "__main__":
  print('hello')