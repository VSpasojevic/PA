import sys


from enum import Enum	

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        
        
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		


class Edge:
    def __init__(self, s= None, d=None, w=None):
        self.source = s
        self.destination = d
        self.weight = w






if __name__=="__main__":


    s = Vertex(c=VertexColor.WHITE, d1=1)
    t = Vertex(c=VertexColor.WHITE, d1=2)
    x = Vertex(c=VertexColor.WHITE, d1=3)
    y = Vertex(c=VertexColor.WHITE, d1=4)
    z = Vertex(c=VertexColor.WHITE, d1=5)
    

    lista=list()

    lista.append([s,t,y])
    lista.append([t,x,y])
    lista.append([x,z])
    lista.append([y,t,x,z])
    lista.append([z,x,s])
    

    e1 = Edge('s','y',5)
    e2 = Edge('s','t',10)


    e3 = Edge('t','y',2)
    e4 = Edge('t','x',1)

    e5= Edge('x','z',4)

    e6 = Edge('y','z',2)
    e7 = Edge('y','x',9)
    e8 = Edge('y','t',3)
    
    e9 = Edge('z','x',6)
    e10 = Edge('z','s',7)


      
    tezine = list()
    
    tezine.append(e1)
    tezine.append(e2)
    tezine.append(e3)
    tezine.append(e4)
    tezine.append(e5)
    tezine.append(e6)
    tezine.append(e7)
    tezine.append(e8)
    tezine.append(e9)
    tezine.append(e10)




    for i in tezine:
        print(i.source,"->",i.destination,"weight",i.weight)


    #graf
    for i in range (0,len(lista)):
        print("\n")
        for j in range (0,len(lista[i])):
            print(lista[i][j].d1)

