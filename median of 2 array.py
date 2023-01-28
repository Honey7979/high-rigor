N=int(input("enter n numbers:"))
M=int(input("enter m numbers:"))
L=[None]*N
L2=[None]*M
i=0
j=0
while i<N:
    n=int(input())
    L[i]=n
    i+=1
# print(L)
while j<M:
   m=int(input())
   L2[j]=m 
   j+=1
print(L)
print(L2)

Lth=(N+M)
merged_array=(L+L2)

# median

if Lth%2!=0:
    median=(Lth+1/2)
    print("odd",median)
else:
    median=((Lth/2)+(Lth/2+1))/2
    print("even",median)