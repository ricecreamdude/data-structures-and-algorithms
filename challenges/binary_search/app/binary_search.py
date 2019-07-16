def binary_search(arr, key, start, end):
  mid = (start + (end - 1)) // 2
  if end >= start:
    if arr[mid] == key:
      return mid
    if arr[mid] < key:
      return binary_search(arr, key, mid + 1, end)
    if arr[mid] > key:
      return binary_search(arr, key, start,  mid - 1)
  else: 
    return -1

if __name__ == "__main__":
  x = binary_search([1,5,9], 5, 0, len([1,5,9])) 
  print(x)