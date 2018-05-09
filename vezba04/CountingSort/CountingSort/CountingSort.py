import sys


def CountingSort(A,B,k):
    C=[None]*k
    for i in range (0,k,1):
        C[i]=0
    

    for j in range (0,len(A),1):
        C[A[j]]=C[A[j]]+1
    
    print("lenA=",len(A))

    for i in range (0,len(A)-1,1):
        C[i]= C[i]  + C[i-1]
        print("C=",C)
    
    for j in range (len(A)-1,-1,-1):
        B.insert(C[A[j]],A[j])
        C.insert(A[j],C[A[j]]-1)





if __name__=='__main__':
    print("HI")

    A=[2,5,3,0,2,3,0,3]
    B=[]
    print("A=",A)


    CountingSort(A,B,6)
    print("B=",B)

