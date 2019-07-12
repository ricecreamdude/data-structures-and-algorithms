def findFibonacci(findIndex, counter, arr):
  if findIndex <= counter:
    return arr[counter]
  else:
    counter += 1
    pre = 1
    PRE = 0
    if (counter - 1) >= 0:
      pre = arr[ (counter-1) ]
    if (counter-2) >= 0:
      PRE = arr[ counter-2 ]

    arr.append( (pre + PRE) )

    return findFibonacci(findIndex, counter, arr)

if __name__ == "__main__":
  answer = findFibonacci(9,0,[1])
  