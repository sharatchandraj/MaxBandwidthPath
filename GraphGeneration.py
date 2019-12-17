from collections import namedtuple
from random import randint


#avg degree = 2*E/V

from statistics import mean

NumberOfVertices=5000

Edge = namedtuple('Edge', ['vertex', 'weight'])
EdgesMatrix = [[0 for x in range(NumberOfVertices)] for y in range(NumberOfVertices)]

edgesList=[]

vertices=[vertex for vertex in range(0, NumberOfVertices)]
degree=[0]*len(vertices)

class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))
        edgesList.append([weight,source,dest])

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v



def createCycle(graph):
    for v in vertices:
        if(v+1<len(vertices)):
            # print('Creating an edge between', v, 'and', v + 1)
            graph.add_edge(v,v+1,randint(1,1000))
            degree[v]=degree[v]+1
            degree[v+1]=degree[v+1]+1
            EdgesMatrix[v][v+1]=1
            EdgesMatrix[v+1][v]=1
        else:
            # print('Creating an edge between', v, 'and', 0)
            graph.add_edge(v,0,randint(1,1000))
            degree[v]=degree[v]+1
            degree[0]=degree[0]+1
            EdgesMatrix[v][0]=1
            EdgesMatrix[0][v]=1



def addRandomEdge(graph):
    vertex1=randint(0,NumberOfVertices-1)
    vertex2=randint(0,NumberOfVertices-1)
    weight=randint(1,1000)
    if(EdgesMatrix[vertex1][vertex2]==0 and vertex1!=vertex2):
        graph.add_edge(vertex1,vertex2,weight)
        degree[vertex1]=degree[vertex1]+1
        degree[vertex2]=degree[vertex2]+1
        EdgesMatrix[vertex1][vertex2]=1
        EdgesMatrix[vertex2][vertex1]=1
    else:
        addRandomEdge(graph)



def generateSparseGraph():
    global edgesList, degree, EdgesMatrix
    edgesList=[]
    degree = [0] * len(vertices)
    EdgesMatrix = [[0 for x in range(NumberOfVertices)] for y in range(NumberOfVertices)]
    print('Number of Vertices',NumberOfVertices)
    g=GraphUndirectedWeighted(len(vertices))

    createCycle(g)

    remainingEdges=int((6*NumberOfVertices)/2-NumberOfVertices)

    #add remaining edges
    for i in range(remainingEdges):
        addRandomEdge(g)

    print('Average degree of graph',mean(degree))



    return g,edgesList

def generateDenseGraph():
    global edgesList,degree,EdgesMatrix
    edgesList=[]
    degree = [0] * len(vertices)
    EdgesMatrix = [[0 for x in range(NumberOfVertices)] for y in range(NumberOfVertices)]
    print('Number of Vertices', NumberOfVertices)
    g = GraphUndirectedWeighted(len(vertices))

    createCycle(g)

    remainingEdges = int((1000 * NumberOfVertices) / 2 - NumberOfVertices) #1000 for 5000 vertices and 4 for 20

    for i in range(remainingEdges):
        addRandomEdge(g)


    print('Average degree of graph', mean(degree))

    return g, edgesList

