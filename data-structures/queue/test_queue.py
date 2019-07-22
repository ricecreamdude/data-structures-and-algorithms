from .queue import Queue
from .pseudo_queue import PseudoQueue

def test_queue_init():  
  assert Queue

#test enqueue
def test_enqueue_init():
  q = Queue()
  assert q.enqueue

#test dequeue
def test_dequeue_init():
  q = Queue()
  assert q.dequeue

#test peek
def test_peek_init():
  q = Queue()
  assert q.peek

#PseudoCode Test Init
def test_pseudo_enqueue_init():
  pq = PseudoQueue()
  assert pq.enqueue
  
def test_pseudo_enqueue_single():
  pq = PseudoQueue()
  pq.enqueue('one')

  assert pq.addStack.peek() == 'one'
def test_pseudo_enqueue_many():
  pq = PseudoQueue()
  pq.enqueue('one')
  pq.enqueue('two')
  pq.enqueue('three')

  assert pq.addStack.peek() == 'three'



def test_pseudo_dequeue_init():
  pq = PseudoQueue()
  assert pq.dequeue

def test_pseudo_dequeue_single():

  pq = PseudoQueue()
  pq.enqueue('one')
  pq.enqueue('two')
  pq.enqueue('three')

  assert pq.dequeue() == 'one'  

def test_pseudo_dequeue_many():

  pq = PseudoQueue()
  pq.enqueue('one')
  pq.enqueue('two')
  pq.enqueue('three')

  pq.dequeue()
  pq.dequeue()

  node = pq.dequeue() == "three"

  assert node