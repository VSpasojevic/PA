import sys




class Vertex:
    def __init__(self,n = None,d = None, p = None):
        self.name = n
        self.dist = d
        self.parant = p
        #self.edges = ed


class Edge:
    def __init__(self, s=None,d=None,w=None):
        self.source = s
        self.destination = d    
        self.weight = w


def MakeGraph():
   
    G = list()

    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")
    g = Vertex("g")


    G.append([a,b,c])
    G.append([b,d])
    G.append([c,d,e])
    G.append([d,e,f])
    G.append([e,f,g])
    G.append([f,g])
    G.append([g])

    return G



def printGraph(G):
    
    #print("cao")
    #for i in range(0,len(G)):
    #    for j in range(0,len(i)):
    #    print(G[i][j].name)


    for i in range (0,len(G)):
        print("\n")
        for j in range (0,len(G[i])):
            print(G[i][j].name)


def GetOutDegrees(Graph):
    
    outList=list()
    
    for i in range(0,len(G)):
        outList.append(len(G[i])-1) 

    #print(outList)
    return outList



def GetInDegress(G):
    inList = list()
    inList = [0, 0, 0, 0, 0, 0, 0]

    for i in range(0, len(G)):
        for k in range(0, len(G)): 
            for l in range(1, len(G[k])):
                if (G[i][0] == G[k][l]):
                    inList[i] += 1

    return inList;


def initialize_single_source(G,s):
    for vertex in G:
        vertex.dist = math.inf
        vertex.parent = None

    s.dist = 0



#def ShortestPath(G,node1,node2):



if __name__=="__main__":
    print("Hi")

    #lista izlaznih cvorova iz a
    
    G = MakeGraph()


    #print(G)

    printGraph(G)


    #veze

    ab = Edge("a","b",8)
    ac = Edge("a","c",6)

    bd = Edge("b","d",10)

    cd = Edge("c","d",15)
    ce = Edge("c","e",9)

    de = Edge("d","e",14)
    df = Edge("d","f",4)

    ef = Edge("e","f",13)
    eg = Edge("e","g",17)

    fg = Edge("f","g",7)


    edges = list()

    edges.append(ab)
    edges.append(ac)
    edges.append(bd)
    edges.append(cd)
    edges.append(ce)
    edges.append(de)
    edges.append(df)
    edges.append(ef)
    edges.append(eg)
    edges.append(fg)


    for i in edges:
        print (i.source,"-->",i.destination,"weight:", i.weight)

        
    print("In Degrees",GetInDegress(G))

    print("Out Degrees",GetOutDegrees(G))




   