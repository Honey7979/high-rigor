a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print(L) 
i=1
while i<a:
    j=i
    while j>0:
        if L[j-1]>L[j]:
            L[j-1],L[j]=L[j],L[j-1]
        j-=1  
    i+=1
print(L)


