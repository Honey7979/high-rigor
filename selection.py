a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print(L) 
M=0
while M<a:
    mi=i
    j=i+1
    while j < a-1:
        if L[mi]>L[j]:
            mi=j 
        j+=1
    M+=1
    L[i],L[mi] = L[mi],L[i]
print(L)

