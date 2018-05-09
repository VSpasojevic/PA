class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.key = val1
        self.a2 = val2

class TBTS:
    
    def __init__(self, r=None):
        self.root=r
        #self.len=l


def MakeNode(parent,n1,n2):
    
    #prolazi i sa poredjenjem sa jednim if-om kao sto sam prvo i uradio

    if parent.data.key <= n1.data.key:
        n1.parent=parent
        parent.right=n1
    else:
        n2.parent=parent
        parent.left=n1

    if parent.data.key <= n2.data.key:
        n2.parent=parent
        parent.right=n2
    else:
        n2.parent=parent
        parent.left=n2


def PrintNode(node):

    #print("parent:",node.parent.data.key)
    print("levi:",node.left.data.key)
    print("right:",node.right.data.key)



def ThreeInsert(T,z):
    y=None
    x=T.root

    while x is not None:
        y=x
        if z.data.key < x.data.key:
            x=x.left
        else:
            x=x.right
    z.p=y

    if y is None:
        T.root=z
    elif z.data.key < y.data.key:
        y.left=z
    else:
        y.right=z


def InorderThreeWalk(x):
     if x is not None:
         InorderThreeWalk(x.left)
         print("x->key",x.data.key)
         InorderThreeWalk(x.right)
         




d1 = Data(1, 2)
d2 = Data(3, 4)
d3 = Data(5, 6)
d4 = Data(15, 16)

print(d1.key, d1.a2)
print(d2.key, d2.a2)
print(d3.key, d3.a2)




n1=Node(None,None,None,d2)
n2=Node(None,None,None,d1)
n3=Node(None,None,None,d3)
n4=Node(None,None,None,d4)





MakeNode(n1,n2,n3)

PrintNode(n1)

r= TBTS()


ThreeInsert(r,n1)


#print ("n2->key",n2.data.key)

ThreeInsert(r,n2)
ThreeInsert(r,n3)
#ThreeInsert(r,n4)


InorderThreeWalk(n2)


