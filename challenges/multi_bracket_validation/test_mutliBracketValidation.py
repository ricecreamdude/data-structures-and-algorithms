from multiBracketValidation import *

def test_MBV_init():
  mbv = MultiBracketValidation()
  assert mbv

def test_MBV_validates_square_brackets():
  b = MultiBracketValidation()
  assert b.validate('[]') is True
  assert b.validate('[][]') is True
  assert b.validate('[][][]]') is False

def test_MBV_validates_curly_brackets():
  b = MultiBracketValidation()
  assert b.validate('{}') is True
  assert b.validate('{}{}') is True
  assert b.validate('{}{}{}}') is False

def test_MBV_validates_circle_brackets():
  b = MultiBracketValidation()
  assert b.validate('()') is True
  assert b.validate('()()') is True
  assert b.validate('()())') is False

def test_MBV_validates_multiple_bracket_types():
  b = MultiBracketValidation()
  assert b.validate('()[]{}') is True
  assert b.validate('({[]})') is True
  assert b.validate('[){](]') is False

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


