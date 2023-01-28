a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print(L)
k=int(input())
i=0
count=1
m=0
while m<a:
    if L[i]=="0":
        pass
    elif count<k:
        count+=1
    elif count==k:
        print(L[i])
        L[i]=="0"
        m+=1 
        count=1 
        i=(i+1)%a 