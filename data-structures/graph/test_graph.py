"""
1. Node can be successfully added to the graph
2. An edge can be successfully added to the graph
3. A collection of all nodes can be properly retrieved from the graph
4. All appropriate neighbors can be retrieved from the graph
5. Neighbors are returned with the weight between nodes included
6. The proper size is returned, representing the number of nodes in the graph
7. A graph with only one node and edge can be properly returned
8. An empty graph properly returns null

"""
from graph import Graph
from graph import Vertex

import pytest

def test_init_graph_and_vertex():

  assert Graph
  assert Vertex

def test_add_node_to_graph():

  g = Graph()

  test = g.addVertex('potato')

  assert isinstance(test, Vertex)
  assert test in g.vertices
  assert g.vertices[0].value == 'potato'

def test_add_edge_to_graph():

  g = Graph()

  apple = g.addVertex('apple')
  banana = g.addVertex('banana')

  g.addEdge(apple, banana, 50)

  assert g.vertices[0].neighbors[0] == {banana, 50}

def test_add_edge_to_graph():

  g = Graph()

  apple = g.addVertex('apple')
  banana = g.addVertex('banana')

  g.addEdge(apple, banana, 50)

  assert g.vertices[0].neighbors[0] == {banana, 50}

def test_add_edge_to_graph_doesnt_add_non_existant():

  g = Graph()

  apple = g.addVertex('apple')
  answer = g.addEdge(apple, 'banana', 50)

  assert answer == 'Please ensure both v1 and v2 exist in the graph'

def test_get_vertices():

  g = Graph()

  apple = g.addVertex('apple')
  banana = g.addVertex('banana')
  cucumber = g.addVertex('cucumber')
  
  g.getVertices == [apple, banana, cucumber]


def test_get_neighbors():

  g = Graph()

  apple = g.addVertex('apple')
  banana = g.addVertex('banana')
  cucumber = g.addVertex('cucumber')
  durian = Vertex('durian')

  g.addEdge(apple, banana, 45)
  g.addEdge(apple, cucumber, 60)

  assert g.getNeighbors(apple) == [{banana, 45}, {cucumber, 60}]
  assert g.getNeighbors(durian) == 'Provided vertex does not exist in this graph'


def test_graph_length():

  g = Graph()
  h = Graph()

  g.addVertex('apple')
  g.addVertex('banana')
  g.addVertex('cucumber')

  h.addVertex('apple')
  h.addVertex('banana')
  h.addVertex('cucumber')
  h.addVertex('durian')

  assert len(g) == 3
  assert len(h) == 4