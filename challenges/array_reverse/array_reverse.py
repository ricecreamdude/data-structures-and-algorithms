list = str( input("Please enter an array: ") )
list = list.split()
#output
newList = [None] * len(list)

start = 0
end = len(list) -1

print('start: ' + str(start) )
print('end: ' + str(end) )

while start < end:
  newList[start] = list[end]
  newList[end] = list[start]
  start += 1
  end -= 1

print(newList)