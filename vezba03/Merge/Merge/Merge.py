import sys
import math
import random

def MergeSort(A,p,r):
    if p<r:
        q=math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)



def Merge(A,p,q,r):
    n1=int(q)-int(p)
    n2=int(r)-int(q)
    L=[]
    R=[]

    for i in range (n1):
        L[i]=A[p+i]
    for j in range (n2):
        R[j]=A[q+j]

    i=1
    j=1

    for k in range (p,r):
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else :
            j=j+1


def change(a,b):
    temp=a
    a=b
    b=temp


def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range (p,r-1):
        if A[j]<=x:
            i=i+1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
        temp=A[i+1]
        A[i+1]=A[r]
        A[r]=temp
    return i+1

def RandomizedPartition(A,p,r):
    i=random.randint(p,r)
    temp=A[r]
    A[r]=A[i]
    A[i]=temp
    return Partition(A,p,r)


def RandomizedQuick(A,p,r):
    if p < r:
        q=Partition(A,p,r)
        RandomizedQuick(A,p,q-1)
        RandomizedQuick(A,q+1,r)


if __name__=='__main__':
    
    A=[1,5,45,2,36,4]
    
    print("Niz A:",A)
    print("n=",len(A))


    #MergeSort(A,0,len(A)-1)

 
    RandomizedQuick(A,0,len(A)-1)
   # change(a,b)

    print("Soritran niz:",A)
    #print("rand:",random.randint(0,5))



