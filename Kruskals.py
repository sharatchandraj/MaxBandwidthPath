from collections import namedtuple
import HeapSortForKruskals
import MaxHeap

NumberOfVertices = 5000

Edge = namedtuple('Edge', ['vertex', 'weight'])


dad=[None]*NumberOfVertices
rank=[None]*NumberOfVertices
KruskalsEdgesList=[]
T = []
wt = [None] * NumberOfVertices
status=[None]*NumberOfVertices
predecessor=[None]*NumberOfVertices


class SpanningTreeGraphGenerator(object):
    def __init__(self, vertex_count):
        global KruskalsEdgesList
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]
        KruskalsEdgesList=[]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))
        KruskalsEdgesList.append([weight,source,dest])

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v



def MakeSet(vertex):
    dad[vertex]=0
    rank[vertex]=0

def Union(r1,r2):
    if(rank[r1]>rank[r2]):
        dad[r2]=r1
    elif(rank[r2]>rank[r1]):
        dad[r1]=r2
    else:
        dad[r2]=r1
        rank[r1]=rank[r1]+1

def Find(vertex):
    w=vertex
    s=[]
    while(dad[w]!=0 ):
        s.append(w)
        w=dad[w]

    while(len(s)!=0):
        vertex=s.pop()
        dad[vertex]=w

    return w


def Kruskals(graph,source,destination,el):
    global KruskalsEdgesList,T
    T=[]
    KruskalsEdgesList=[]
    KruskalsEdgesList=el
    HeapSortForKruskals.HeapSort(KruskalsEdgesList)
    for i in graph.get_vertex():
        MakeSet(i)

    for edge in KruskalsEdgesList:
        vertex1=edge[1]
        vertex2=edge[2]
        # print(edge,vertex1,vertex2)
        r1=Find(vertex1)
        r2=Find(vertex2)
        if(r1!=r2):
            Union(r1,r2)
            T.append(edge)



    SpanningTreeGraph = SpanningTreeGraphGenerator(NumberOfVertices)


    for e in T:
        SpanningTreeGraph.add_edge(e[1],e[2],e[0])

    MBP,distance = getMBP(SpanningTreeGraph,source,destination)
    return MBP,distance





def getMBP(graph,source,destination):

    MaxHeap.initialize()

    for i in graph.get_vertex():
        status[i] = 'unseen'
        predecessor[i]=None

    status[source] = 'intree'

    for i in graph.get_edge(source):
        status[i.vertex] = 'fringe'
        wt[i.vertex] = i.weight
        MaxHeap.Insert(i.vertex, i.weight)
        predecessor[i.vertex] = source


    while 'fringe' in status:
        destinationFound=False
        v=MaxHeap.Max()
        status[v]='intree'
        MaxHeap.Delete(v)
        for e in graph.get_edge(v):
            if(status[e.vertex]=='unseen'):
                status[e.vertex]='fringe'
                predecessor[e.vertex]=v
                wt[e.vertex]=wt[v] if (wt[v]<e.weight) else e.weight
                MaxHeap.Insert(e.vertex, wt[e.vertex])
            elif (status[e.vertex]=='fringe'and wt[e.vertex]<min(wt[v],e.weight)):
                predecessor[e.vertex]=v
                MaxHeap.Delete(e.vertex)
                wt[e.vertex]=wt[v] if (wt[v]<e.weight) else e.weight
                MaxHeap.Insert(e.vertex, wt[e.vertex])

            if(e.vertex==destination):
                destinationFound=True
                break

        if(destinationFound):break


    maxBWPath = []
    end = destination
    while end is not None:
        maxBWPath.append(end)
        end = predecessor[end]

    maxBWPath.reverse()

    return maxBWPath,wt[destination]

