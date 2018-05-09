import sys
import random
import time



"""
def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 11000, 10000)
"""

def InsertionSort(A):
    
    for j in range(1,len(A)):
        key=A[j];
        i=j-1
        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
            A[i+1]=key





def BubbleSort(A):
        
   
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                temp=A[i]
                A[i]=A[j]
                A[j]=temp


def pretraga(A,t):
    #index=A[0]    
    for i in range(len(A)):
        if A[i]==t:
            index=i
    print("Trazeni broj je : ", t, "i njegov index je :",index)




def pretragaBinarno(A,t):
    prvi=0
    srednji=len(A)/2
    poslednji=len(A)
    index=0
    while poslednji>=prvi: 
        if A[int(srednji)]==t:
            index=int(srednji)
            return
        else:
            if t>A[int(srednji)]:
                prvi=srednji+1
                srednji=(srednji+poslednji)/2
                poslednji=poslednji
                 
            else:
                prvi=0
                srednji=(srednji+prvi)/2
                poslednji=srednji
        

    print("Binarna pretraga index:",index)
    
    

#main
if __name__=='__main__':
    #print("Sortintan niz")
    A=[1,531,312,4,3,12,18]



    B=[]

    trazena=sys.argv[len(sys.argv)-1]
    print("T=",trazena)
    
    for i in range(1,len(sys.argv)-1):
       B.append(int(sys.argv[i]))


    #print("B= ",B)

    #print("numArg: ",len(sys.argv))
    BubbleSort(A)
    print("Sortintan niz",A)

    #pretraga(B,5)
    pretragaBinarno(A,3)



    

    

















