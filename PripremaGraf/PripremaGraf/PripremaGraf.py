import sys

import math

class Vertex:
    def __init__(self,p = None, n = None, d = None):
        self.name = n
        self.parent = p
        self.data = d
        self.neighbours = list()



class Edges:
    def __init__(self, s = None, d = None, w = None):
        self.source = s
        self.destination = d
        self.weight = w



class Graph:
    def __init__(self,ver = None, ed = None):
        self.vertices = ver
        self.edges = ed

def MakeGraph():
    
    a = Vertex(n = "a")
    b = Vertex(n = "b")
    c = Vertex(n = "c")
    d = Vertex(n = "d")
    e = Vertex(n = "e")
    f = Vertex(n = "f")
    g = Vertex(n = "g")

    a.neighbours.append(b)
    a.neighbours.append(c)

    b.neighbours.append(d)

    c.neighbours.append(d)
    c.neighbours.append(d)

    d.neighbours.append(e)
    d.neighbours.append(f)

    e.neighbours.append(f)
    e.neighbours.append(g)

    f.neighbours.append(g)

    # ubacimo sve cvorove u jednu listu cvorova
    v = [a,b,c,d,e,f,g]

    #edges

    #ubacuj objekte u ivice a ne stringove!!!! 

    e1= Edges(a,b,8)
    e2= Edges(a,c,6)

    e3= Edges(b,d,10)

    e4= Edges(c,d,15)
    e5= Edges(c,e,9)

    e6= Edges(d,e,14)
    e7= Edges(d,f,4)

    e8= Edges(e,f,13)
    e9= Edges(e,g,17)

    e10= Edges(f,g,7)

    #stavimo i sve ivice u listu

    e = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]

    g = Graph(v,e)

    return g
    


def printGraph(g):
    for i in g.vertices:
        print(i.name)



def GetInDegrees(g):
    #lista povratnih vrednosti

    ret = list()

    for i in g.vertices:
        counter = 0
        for j in g.edges:
            if  i.name == j.destination.name: 
                counter += 1
        ret.append(counter)


    return ret

def GetOutDegrees(g):
    #d = dict()
    lista = list()
    for i in g.vertices:
        #d.update({i.name:0})
        counter = 0
        for j in g.edges:
            if i.name == j.source.name:
                counter += 1
        lista.append(counter)


    return lista


#data=distance
# data is mine, d is in documentation :D


def initalize_single_source(g,s):

    for v in g.vertices:
        v.data = math.inf
        v.parent = None
    s.data =0


def w(u,v,e):
    for i in e:
        if i.source == u:
            if i.destination == v:
                w = i.weight

    return w


#vertex , vertex, edges

def relax(u,v,e):
   #zasto izbacuje ovde gresku????
   # w = w(u,v,e)

    if v.data > u.data + w(u,v,e):
        v.data = u.data + w(u,v,e)
        v.parent = u

#graph , edges, vertex(source)
def Bellman_Ford(g,e,s):
    initalize_single_source(g,s)
    for i in range (len(g.vertices)-1):
        for edge in g.edges:
            relax(edge.source,edge.destination,e)


    for edge in g.edges:
        if edge.destination.data > edge.source.data + edge.weight:
            return False
    return True



#       s -> source, v -> destinaion
def prinPath(g,s,v):
    global path
    global length

    length = 0
    path = list()

    #ako cvor koji gledamo ne povezuje nista

    if v==s:
        path.append(s.name)
    elif v.parent == None:
        print("No path form", s.name, "-->",v.name, "exist")
    else:
        prinPath(g,s,v.parent)
        length += w(v.parent,v,g.edges)
        path.append(v.name)
    
def ShortestPath(g,nodeA,nodeB):
    global path
    global length

    Bellman_Ford(g,g.edges,nodeA)
    prinPath(g,nodeA,nodeB)
    print("Shortest path from ",nodeA.name," to",nodeB.name,"with length :")
    print("(",path," ",length,")")

#proveravam u listi ivica da li postoji veza izmedju dva cvora

def EdgeExist(nodeA,nodeB,e):
    for i in e:
        #pazi da je nodeA klase VERTEX pa mora da se uzme njegovo polje name!!!!!!!!!!!
        if nodeA.name == i.source.name:
            if nodeB.name == i.destination.name:
                return True
    return False


def ChangeWeight(nodeA,nodeB,e,newWeight):
    for i in e:
        if nodeA.name == i.source.name:
            if nodeB.name == i.destination.name:
                i.weight = newWeight

def UpdateEdge(g,nodeA,nodeB,w):
    if EdgeExist(nodeA,nodeB,g.edges):
        ChangeWeight(nodeA,nodeB,g.edges,w)
    else:
        new_edge = Edges(nodeA,nodeB,w)
        graph.edges.append(new_edge)


def NewShortestPath(g):
    global path
    global length
    
    nodeA = g.vertices[1]
    nodeB = g.vertices[2]
    nodeC = g.vertices[6]

    UpdateEdge(g,nodeA,nodeB,-4)

     

    Bellman_Ford(g,g.edges,g.vertices[0])
    prinPath(g,g.vertices[0],g.vertices[6])
    print("Shortest path from ",g.vertices[0].name," to",nodeC.name,"with length :")
    print("(",path," ",length,")")




################################        main   ################################################

if __name__=="__main__":
    print("Vertex:")

    
    graph = MakeGraph()

    printGraph(graph)
    # napravio sam graf :D

    l1 = GetInDegrees(graph)
    
    print("GetInDegrees:",l1)

    l2 = GetOutDegrees(graph)
    
    print("GetOutDegrees:",l2)

    nodeA = graph.vertices[0]   #a
    nodeB = graph.vertices[6]   #g
    nodeC = graph.vertices[1]   #b
    nodeD = graph.vertices[3]   #d
    nodeE = graph.vertices[2]   #c

    #radi i shortest path :D
    ShortestPath(graph,nodeA,nodeB)

    #ostali samo 4. i 5. da se odrade
    UpdateEdge(graph,graph.vertices[1],graph.vertices[2],-6)

    NewShortestPath(graph)

    #print("Update b-->c")
    
    #for j in graph.edges:
    #    if j.source == nodeC:
    #        if j.destination == nodeE:
    #            print("Tezina: ",j.weight)
#
 #   ShortestPath(graph,nodeA,nodeB)