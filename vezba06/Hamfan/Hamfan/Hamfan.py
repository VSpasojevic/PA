import sys
import operator

def GetHistogram(list):
    d=dict()
    for key in list:
        if (key in d):
            d[key]+=1
        else:
            d[key]=1
        
    #print(d)
    return d


class Data:
    def __init__(self, val,fre):
        
        self.value=val
        self.freq=fre




class Node:
    
    def __init__(self, p = None, l = None, r = None, f = None):
       
        self.parent = p
        self.left = l
        self.right = r
        self.freq = f

    #sort list
def GetMinFreqElem(list):
    tmp=list[0].freq,list[1].freq
    #brisanje elemenata liste
    del  (list,0)
    del  (list,1)    

    return tmp


if __name__=='__main__':
    
    #print("Hi")
    input1 = ['a', 'b']
    #print(input1)

    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']

    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']

    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']

    dic={}
    dic=GetHistogram(input4)
    print(dic)
    
    

    #dict to list

    l=[]
    #sort list
    l=sorted(dic.items(), key=operator.itemgetter(1))
    print("Sorted list",l)
    
    size=len(l)


    #list object
    lObject=[]
    for value,frequence in l:
         lObject.append(Data(value,frequence))
    


    min=GetMinFreqElem(lObject)
    print(min)
   #n1=Node(None,lObject[0],lObject[1],lObject[0]+lObject[1])

