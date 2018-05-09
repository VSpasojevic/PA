from enum import Enum	
import sys
import math

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None, i = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.id = i 

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		


def printLista(lista):
     for i in range (0,len(lista)):
        
        print("\n")
        
        for j in range (0,len(lista[i])):
            #print("->",lista[i][j].id)
            print(lista[i][j].id)


class Graph:
    def __init__(self, g = None):
        #graph mi je lista cvorova 
        self.graph=g

def BFS(G,s):
    for u in G.graph:
        for i in range (0,len(G.graph[u])):
            u[i].c = WHITE
            u[i].d = math.inf
            u[i].d1 = None
           
           

        
        

if __name__=='__main__':
    print("Cvorovi")
    
    u1 = Vertex(c=VertexColor.WHITE, d1=11, d2=21,i=1)    
    u2= Vertex(c=VertexColor.WHITE, d1=12, d2=22,i=2)    
    u3 = Vertex(c=VertexColor.WHITE, d1=13, d2=23,i=3)    
    u4= Vertex(c=VertexColor.WHITE, d1=14, d2=24,i=4)    
    u5 = Vertex(c=VertexColor.WHITE, d1=15, d2=25,i=5)    


    #v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)


    print(u1.d1,u1.d2,u1.id)
    print(u2.d1,u2.d2,u2.id)
    print(u3.d1,u3.d2,u3.id)
    print(u4.d1,u4.d2,u4.id)
    print(u5.d1,u5.d2,u5.id)


    lista = list()
    
    l1 = list()
    l2 = list()
    l3 = list()
    l4 = list()
    l5 = list()

    l1.append(u1)
    l1.append(u2)
    l1.append(u5)


    l2.append(u2)
    l2.append(u5)
    l2.append(u3)
    l2.append(u4)

    l3.append(u3)
    l3.append(u2)
    l3.append(u4)



    l4.append(u4)
    l4.append(u2)
    l4.append(u5)
    l4.append(u3)

    l5.append(u5)
    l5.append(u4)
    l5.append(u1)
    l5.append(u3)


    lista.append(l1)
    lista.append(l2)
    lista.append(l3)
    lista.append(l4)
    lista.append(l5)

    #lista cvorova

    print ("Lista")
    
    printLista(lista)

    #lista[0].append(u2,u5)

   
    ''' 
    gra=Graph(lista)

    print ("Graf")
    print (gra.graph)
    '''
    
    



