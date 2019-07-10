def binary_search(arr, key, start, end):
  start = start or 0
  end = len(arr) or 0

  mid = start + (end - 1) // 2
  if arr[mid] == key:
    return mid
  if arr[mid] < key:
    return binary_search(arr, key, mid, end)
  if arr[mid] > key:
    return binary_search(arr, key, start, mid)

if __name__ == "__main__":
  x = binary_search([1,5,9], 5, 0, len([1,5,9])) 
  print(x)