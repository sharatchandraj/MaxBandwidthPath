from collections import namedtuple
import MaxHeap


NumberOfVertices=5000

Edge = namedtuple('Edge', ['vertex', 'weight'])
status = [None] * NumberOfVertices
wt = [None] * NumberOfVertices


def DijkstrasWithHeap(graph, source, destination):

    MaxHeap.initialize()

    dad=[None]*NumberOfVertices
    for i in graph.get_vertex():
        status[i]='unseen'

    status[source]='intree'

    for i in graph.get_edge(source):
        status[i.vertex]='fringe'
        wt[i.vertex]=i.weight
        MaxHeap.Insert(i.vertex, i.weight)
        dad[i.vertex]=source


    while 'fringe' in status:
        destinationFound=False
        v=MaxHeap.Max()
        if(v==destination): break
        status[v]='intree'
        MaxHeap.Delete(v)
        for e in graph.get_edge(v):
            if(status[e.vertex]=='unseen'):
                status[e.vertex]='fringe'
                dad[e.vertex]=v
                wt[e.vertex]=wt[v] if (wt[v]<e.weight) else e.weight
                MaxHeap.Insert(e.vertex, wt[e.vertex])
            elif (status[e.vertex]=='fringe'and wt[e.vertex]<min(wt[v],e.weight)):
                dad[e.vertex]=v
                MaxHeap.Delete(e.vertex)
                wt[e.vertex]=wt[v] if (wt[v]<e.weight) else e.weight
                MaxHeap.Insert(e.vertex, wt[e.vertex])





    maxBWPath =[]
    end = destination
    while end is not None:
        maxBWPath.append(end)
        end = dad[end]

    maxBWPath.reverse()

    return maxBWPath, wt[destination]





