import sys
import math

def Parent(i):
    return i/2



def Left(i):
    return 2*i+1

def Right(i):
    return 2*i




def Max_Heapify(A,i,A_heap_size):
    l=Left(i)
    r=Right(i)
    
    if(l<= A_heap_size and A[l]>A[i]):
        largest=l
        print("lar",largest)
    else:
        largest=i
    if(r <= A_heap_size and A[r] > A[largest]):
        largest=r

    if(largest!=i):
        temp=A[i]
        A[i]=A[largest]
        A[largest]=temp
        Max_Heapify(A,largest,A_heap_size)
        

def Build_Max_Heap(A):
    A_heap_Size=len(A)
    print("A_heap=",A_heap_Size)
    for i in range (math.floor(A_heap_Size/2),0,-1):
        #print("i=",i)
        Max_Heapify(A,i,A_heap_Size)


def HEAPSORT(A):
    Build_Max_Heap(A)
    for i in range(len(A)-1,0,-1):
        temp=A[0]
        A[0]=A[i]
        A[0]=temp

        A_Heap_Size=A_Heap_Size-1

        Max_Heapify(A,1,A_Heap_Size)



if __name__=='__main__':

    print("Hi")


    A=[12,45,1,2,3,456,78,56]

    print("A:",A)
    HEAPSORT(A)
    print("Sortiran niz:",A)
