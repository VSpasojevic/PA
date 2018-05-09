import sys
import math


class Data:
    def __init__(self,key,lit):
        self.key=key
        self.literal=lit

      
def divisionMethod(n,k):
    return k % n



def hashInsert(t,el):

    index=divisionMethod(10,el.key)

    strIndex=str(index)

    #t[el.key]=el.literal

    #l=[t[el.key]]

    #print(l)
    '''l=list()
    l=[t]

    print(l)
    '''

    if strIndex in t:
        t[strIndex]=[t[strIndex],el.literal]
        #l.append(el.literal)
    else:
        t[strIndex]=el.literal


def hashSearch(t,key):


    strKey=str(key)

    if strKey in t:
        print("Trazeni element sa kljucem ",key, "je",t[strKey])
    else:
        print("Nema trazenog elementa sa kljucem",key) 




def hashDelete(t,el):
    
    index=divisionMethod(10,el.key)
    strKey=str(index)
    
    if strKey in t:
        #treba da proverim da li mi je element lista, ako je lista onda moram posebno da se prosetam kroz nju i da nadjem element

        print("Izbrisan element sa kljucem",strKey)
        del t[strKey]
    else:
        print("Nema elementa u listi")


if __name__=='__main__':
    
    #l=list()

    table=dict()

    d=Data(1,'aa')
    d5=Data(1,'mm')
   
    d1=Data(1,'bb')
    d2=Data(1,'dd')
    d3=Data(13,'CC')
    d4=Data(15,'zz')
    d8=Data(154,'aazz')

    #table[d.key]=d.literal

    hashInsert(table,d)
    hashInsert(table,d1)
    hashInsert(table,d2)
    hashInsert(table,d3)
    hashInsert(table,d4)
    hashInsert(table,d5)

    print("Pocetna tabela:")
    print(table)


    hashSearch(table,3)
    hashSearch(table,4)

    hashDelete(table,d4)

    hashDelete(table,d8)


    print(table)
