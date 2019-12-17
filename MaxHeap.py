# file for max heap structure routines

NumberOfVertices=5000
#each element H[i] gives the name of the vertex
H=[-1] #using a list for the heap

#to find the value of a vertex H[i] in the heap, we can use D[H[i]]
D=[None]*NumberOfVertices # list D hold the vertex values

positions =[None]*NumberOfVertices

NNodes=0

def initialize():
    global H,D,positions,NNodes
    H = [-1]
    D = [None] * NumberOfVertices

    positions = [None] * NumberOfVertices
    NNodes=0

def PercolateUp(k):
    parent = int(k/2)
    assert k<len(H),print(k,len(H))
    if(len(H)==2 ):positions[H[k]]=k
    while parent>0:
        if(D[H[k]]>D[H[parent]]):

            tempPosition = positions[H[parent]]
            positions[H[parent]] = positions[H[k]]
            positions[H[k]] = tempPosition

            temp = H[parent]
            H[parent]=H[k]
            H[k]=temp

            k=parent
        else:

            break
        parent = int(k/2)

def PercolateDown(k):

    global NNodes
    while(2*k<=NNodes): #checking if node at k has children
        child1 = 2*k
        child2 = 2*k+1
        if(child2<=NNodes): #checking if k has 2 children
            if(D[H[k]]>D[H[child1]] and D[H[k]]>D[H[child2]]):
                # positions[H[k]]=k
                break
            else:
                if (D[H[child1]]>D[H[child2]]): #child1 is bigger

                    tempPosition = positions[H[k]]
                    positions[H[k]] = positions[H[child1]]
                    positions[H[child1]] = tempPosition

                    temp =H[k]
                    H[k]=H[child1]
                    H[child1]=temp

                    k=child1


                else: #if(D[H[child1]]<D[H[child2]]): #child2 is bigger

                    tempPosition = positions[H[k]]
                    positions[H[k]] = positions[H[child2]]
                    positions[H[child2]] = tempPosition

                    temp = H[k]
                    H[k] = H[child2]
                    H[child2] = temp

                    k = child2

        else:
            if(D[H[k]]>D[H[child1]]):
                break
            else:
                tempPosition = positions[H[k]]
                positions[H[k]] = positions[H[child1]]
                positions[H[child1]] = tempPosition

                temp = H[k]
                H[k]=H[child1]
                H[child1]=temp

                k= child1




def Max():
    return H[1]

def Insert(value,weight):
    global NNodes
    D[value] = weight
    H.append(value)
    NNodes = NNodes + 1
    positions[value] = NNodes
    PercolateUp(NNodes)

def Delete(vertex):
    global NNodes,H
    index=positions[vertex]

    assert index!=None , print (H,vertex,)

    deletedValue =H[index] #save deleted value for the return statement

    positions[H[NNodes]]=index
    positions[deletedValue]=None
    H[index] = H[NNodes] # replace H[index] with the last element in the heap

    NNodes=NNodes-1

    if (NNodes == 1): positions[H[index]] = 1
    positions[vertex]=None
    parent = int(index/2)

    if(index==1 or D[H[parent]]>D[H[index]]):
        PercolateDown(index)
    else:
       
        PercolateUp(index)

    H = H[:-1]
    D[deletedValue] = None
    









