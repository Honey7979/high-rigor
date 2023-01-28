a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print(L)
# marks=[10,5,20,8,30]
# output=[5,8,10,20,30]
i=0
while i<a:
   j=0
   while j+1<len(L):
      if L[j] > L[j+1]:
         L[j],L[j+1] = L[j+1],L[j]

      j+=1
   i+=1
      
print(L)
      
         