a=int(input("enter n numbers:"))
b=int(input("enter m numbers:"))
L=[None]*a
L2=[None]*b
i=0
j=0
e=[]
while i<a:
    n=int(input())
    L[i]=n
    i+=1
while j<b:
   m=int(input())
   L2[j]=m 
   j+=1
print(L)
print(L2)
m=0
d=0
while m<a and d<b:
   if L[m]<L2[d]:
      e.append((L[m]))
      m+=1
   elif L[m]>L[d]:
      e.append((L[d]))
      d+=1
   else:
      e.append((L2[d]))
      d+=1
while m<a:
   e.append((L[m]))
   m+=1
while d<b:
   e.append((L2[d]))
   d+=1
print(e)
