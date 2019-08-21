from animal_shelter import *


def test_animal_shelter_init():
  shelter = AnimalShelter()

  assert shelter

def test_enqueue():
  shelter = AnimalShelter()
  catOne = Cat()
  catTwo = Cat()
  dogOne = Dog()

  shelter.enqueue(catOne)
  shelter.enqueue(catTwo)
  shelter.enqueue(dogOne)

  assert shelter.head is catOne
  assert shelter.head.next is catTwo
  assert shelter.head.next.next is dogOne
  assert shelter.head.next.next.next is None 


def test_dequeue_removes_first_of_type():
#   shelter = AnimalShelter()
#   catOne = Cat()
#   catTwo = Cat()
#   dogOne = Dog()

#   shelter.enqueue(dogOne)
#   shelter.enqueue(catOne)
#   shelter.enqueue(catTwo)

#   shelter.pref_dequeue("cat")

  assert shelter.head is dogOne
  assert shelter.head.next is catTwo

def test_dog_init():
  dog = Dog()
  
  assert dog.value is "dog"

def test_cat_init():
  cat = Cat()

  assert cat.value is "cat"