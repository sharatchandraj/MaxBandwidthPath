import DijkstrasWithHeap
import DijkstrasNoHeap
import Kruskals
import GraphGeneration
import time
from random import randint

def iteration(sg,dg,sparseEdgeList,denseEdgeList):
    source = randint(0, 4999)
    destination = randint(0, 4999)
    print('source:',source,'\t','destination',destination)
    print('Length of sparse edge list',len(sparseEdgeList))
    print('Length of dense edge list',len(denseEdgeList))
    ####################################SPARSE########################

    start = time.clock()
    MBP_NoHeap, distanceNH = DijkstrasNoHeap.DijkstrasNoHeap(sg, source, destination)
    print('For a sparse graph, no Heap took', time.clock() - start)

    start = time.clock()
    MBP_WithHeap, distanceH = DijkstrasWithHeap.DijkstrasWithHeap(sg, source, destination)
    print('For a sparse graph, Heap took', time.clock() - start)

    start = time.clock()
    MBP_Kruskals, distanceK = Kruskals.Kruskals(sg, source, destination, sparseEdgeList)
    print('For a sparse graph, Kruskals took', time.clock() - start)

    if (MBP_NoHeap == MBP_WithHeap == MBP_Kruskals):
        print('Paths match for Sparse Graph')

    if (distanceH == distanceNH == distanceK):
        print('DISTANCES MATCH FOR SPARSE GRAPH')
        print(distanceK)


#############################Dense Graph##########################################


    start = time.clock()
    MBP_NoHeap, distanceNH = DijkstrasNoHeap.DijkstrasNoHeap(dg, source, destination)
    print('For a dense graph, No Heap took', time.clock() - start)

    start = time.clock()
    MBP_WithHeap, distanceH = DijkstrasWithHeap.DijkstrasWithHeap(dg, source, destination)
    print('For a dense graph, Heap took', time.clock() - start)

    start = time.clock()
    MBP_Kruskals, distanceK = Kruskals.Kruskals(dg, source, destination, denseEdgeList)
    print('For a dense graph, Kruskals took', time.clock() - start)

    if (MBP_NoHeap == MBP_WithHeap == MBP_Kruskals):
        print('Paths match for Dense Graph')

    if (distanceH == distanceNH == distanceK):
        print('DISTANCES MATCH FOR DENSE GRAPH')
        print(distanceK)



def main():

    for i in range(5):
        print('********************Graph',i,'*******************************')
        sg,sparseEdgesList=GraphGeneration.generateSparseGraph()
        dg,denseEdgesList=GraphGeneration.generateDenseGraph()
        print('Graphs generated')
        for j in range(5):
            print('********************ITERATION',j,'*****************')
            iteration(sg,dg,sparseEdgesList,denseEdgesList)



if __name__=='__main__':
    main()