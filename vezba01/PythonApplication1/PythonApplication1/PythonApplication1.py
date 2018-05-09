import sys

def sum(n):
    s=0;
    for i in range(n+1):
        s+=i
        
    print("s1= ",s)
        

def kvad(n1):
    s=0;
    for i in range(n1+1):
        s+=i*i
    print("s1= ",s)

def str(str1,str2):
    s1=sys.argv[1]
    s2=sys.argv[2]
    #s3=s1[0]+s1[1]+s2[2]+s1[0]+s1[1]+s2[2]+s2[2]+s2[3]+s2[4]
    s3=s1[0:3]+s1[0:3]+s2[len(s2)-2:len(s2)]
    print("spojeno: ",s3)
    #print("spojeno: ",s2[3])
    
def lista():
    l=[]
    i=100;
    while i>0:
        i-=1
        l.append(i)
    print("lista: ",l)
    
def pon():
    
    fin=open("dict_test","r")
    d=dict()
    for line in fin:
        print("line: ",line)
      

if __name__ == '__main__':
#    print("agr1: ",sys.argv[1])
#    print("agr2: ",sys.argv[2])
#    s1=sys.argv[1]
#    s2=sys.argv[2]
   
    
    #x=int(sys.argv[1])
    #sum(x)
    #kvad(x)
    #str(s1,s2)
    #lista()
    pon()
    

       
