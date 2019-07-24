from multiBracketValidation import *

def test_MBV_init():
  mbv = MultiBracketValidation()
  assert mbv

# def test_MBV_split_string():
#   mbv = MultiBracketValidation()
#   assert mbv.validate('[') == ['[',']'] 

def test_square_bracket_init():
  b = SquareBracket()
  assert b.open is '['
  assert b.close is ']'

def test_curly_bracket_init():
  b = CurlyBracket()
  assert b.open is '{'
  assert b.close is '}'

def test_circle_bracket_init():
  b = CircleBracket()
  assert b.open is '('
  assert b.close is ')'


