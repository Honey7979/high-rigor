a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print(L)
K=int(input())
m=0
j=1
while m<a:
    while j>0:
        if L[m]+L[j]==K:
            print(L[m],L[j])
        j+=1
    m+=1