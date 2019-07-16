from app.fibonacci import findFibonacci

try:
  def test_init():
    assert findFibonacci

  def test_one():
    expect = 1
    actual = findFibonacci(1,0,[1])
    assert actual == expect

  def test_nine():
    expect = 55
    actual = findFibonacci(9,0,[1])
    assert actual == expect
except:
  print('something wrong!')


