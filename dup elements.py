a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print(L) 
k=0
while k<a-1:
   p=k+1 
   if L[k]==L[p]:
       print(L[k])
   k+=1
# a=int(input("enter a number:")) 
# L=[None]*a
# i=0
# while i<a:
#     n=int(input())
#     L[i]=n
#     i+=1
# print(L) 
# i=n-1 
# while i<a:
#     print(L[i],end="")
#     i-=1