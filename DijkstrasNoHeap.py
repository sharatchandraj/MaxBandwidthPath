
from collections import namedtuple
import time
import GraphGeneration

Edge = namedtuple('Edge', ['vertex', 'weight'])

NumberOfVertices=5000

status = [None] * NumberOfVertices
wt = [None] * NumberOfVertices



def pickBestVertex():
    bestweight=0
    bestvetex=None

    for i in range(len(status)) :
        if status[i] is 'fringe' and wt[i]>bestweight:
            bestweight = wt[i]
            bestvetex = i

    return bestvetex





def DijkstrasNoHeap(graph, source, destination):


    dad=[None]*NumberOfVertices

    for i in graph.get_vertex():
        status[i]='unseen'

    status[source]='intree'

    for i in graph.get_edge(source):
        status[i.vertex]='fringe'
        wt[i.vertex]=i.weight
        dad[i.vertex]=source


    while 'fringe' in status:

        v=pickBestVertex()
        status[v]='intree'
        # print ('The best fringe is',v)
        for e in graph.get_edge(v):
            if(status[e.vertex]=='unseen'):
                status[e.vertex]='fringe'
                dad[e.vertex]=v
                wt[e.vertex]=wt[v] if (wt[v]<e.weight) else e.weight
            elif (status[e.vertex]=='fringe'and wt[e.vertex]<min(wt[v],e.weight)):
                dad[e.vertex]=v
                wt[e.vertex]=wt[v] if (wt[v]<e.weight) else e.weight


    maxBWPath =[]
    end = destination
    while end is not None:
        maxBWPath.append(end)
        end = dad[end]

    maxBWPath.reverse()

    return maxBWPath, wt[destination]




##################################################################################



