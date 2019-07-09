
#Import the function from the application
from app.array_shift import array_shift

#First assert that the function you are importing exists

#Then, begin testing the function with various test cases 
def test_should_return_list():
  actual = array_shift([1], 1)
  assert isinstance(actual, (list,)) == True 

def test_insert_to_middle():
  expected = [1,2,3]
  actual = array_shift([1,3], 2)

  assert expected == actual