from app.binary_search import binary_search

def test_function_exists(): 
  assert binary_search

def test_returns_index():
  
  expected = 2
  actual = binary_search([1,5,9], 9, 0, len([1,5,9]))

  assert expected == actual
  

def test_short_array():

  expected = 0
  actual = binary_search([1,5], 1, 0, 2)

  assert expected == actual