import math

def array_shift(arr, val):
  half = math.ceil( len(arr) / 2 )
  
  return arr[:half] + [val] + arr[half:]