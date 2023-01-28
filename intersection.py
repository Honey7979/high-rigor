x=int(input("enter x numbers:"))
y=int(input("enter y numbers:"))
L1=[None]*x
L2=[None]*y
i=0
j=0
while i<x:
   n=int(input())
   L1[i]=n
   i+=1
while j<y:
   p=int(input())
   L2[j]=p
   j+=1
print(L1)
print(L2)
m=0 
L3=[]
while m<x:
    k=0
    while k<y:
        if L1[m]==L2[k]:
            L3.append(L2[k])
        k+=1
    m+=1
print(L3)
   
         


   
         

