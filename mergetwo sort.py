a=int(input("enter n numbers:"))
b=int(input("enter m numbers:"))
L=[None]*a
L2=[None]*b
m=0
n=0
while m<a:
    n1=int(input())
    L[m]=n1
    m+=1
# print(L)
while n<b:
    m1=int(input())
    L2[n]=m1 
    n+=1
print("list1",L)
print("list2",L2)
l2=L+L2 
print(l2)
b=len(l2)
i=0
while i<b:
   j=0
   while j+1<b:
      if l2[j] > l2[j+1]:
         l2[j],l2[j+1] = l2[j+1],l2[j]

      j+=1
   i+=1
      
print(l2)