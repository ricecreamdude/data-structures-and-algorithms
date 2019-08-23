"""
AddVertex()
  Adds a new vertex to the graph
  Takes in the value of that vertex
  Returns the added vertex
AddEdge()
  Adds a new edge between two nodes in the graph
  Include the ability to have a “weight”
  Takes in the two nodes to be connected by the edge
  Both nodes should already be in the Graph
GetNodes()
  Returns all of the nodes in the graph as a collection (set, list, or similar)
GetNeighbors()
  Returns a collection of nodes connected to the given node
  Takes in a given node
  Include the weight of the connection in the returned collection
Size()
  Returns the total number of nodes in the graph
"""

class Vertex:
  def __init__(self, value):
    self.value = value
    self.neighbors = []

class Graph:

  def __init__(self):
    self.vertices = []

  def addVertex(self, value):

    x = Vertex(value)

    self.vertices.append(x)

    return x
  
  def addEdge(self, v1, v2, weight):

    if v1 in self.vertices and v2 in self.vertices: 
      v1.neighbors.append( {v2, weight} )
      return
    
    return 'Please ensure both v1 and v2 exist in the graph'


  #Infomation Retreival Functions
  def getVertices(self):
    return self.vertices

  def getNeighbors(self, vertex):

    if vertex in self.vertices:
      return vertex.neighbors

    return 'Provided vertex does not exist in this graph'

  def __len__(self):
    return len(self.vertices)