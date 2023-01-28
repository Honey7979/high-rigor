a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print("unsorted list",L)

# searching element
x=int(input())
i=0
while i<len(L):
  j=0
  while j+1<len(L):
      if L[j] > L[j+1]:
         L[j],L[j+1] = L[j+1],L[j]

      j+=1
  i+=1     
print("List after sorting",L)
low=0
high=len(L)-1
# FIND THE MIDDLE ELEMENT-
while low<high:
    mid=(low+high)//2

    if x==L[mid]:
        print("mid","Index",mid,L[mid])
        break
    if x==L[low]:
        print("x equal to low")
        print("Index",low,"element",L[low])
        break
    if x==L[high]:
        print("x equal to  high")
        print("Index",high,"elemnt",L[high])
        break
    else:
        if x>L[mid]:
            low=mid+1
        else:
            high=mid-1
else:
    print("NOt found")

    
    

    

