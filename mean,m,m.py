a=int(input("enter n numbers:"))
L=[None]*a
i=0
while i<a:
    n=int(input())
    L[i]=n
    i+=1
print(L)
j=1
sum=0
while j<a:
    sum+=L[j]
    j+=1
print("sum of a list",sum)

# mean
mean=sum/a
print("mean",mean)

# MEDIAN
# formula
# ODD=(N+1)/2
# EVEN=(N/2)+(N/2)+1
if a%2!=0:
    m=(a+1)/2
    print("median",m)
else:
    if a%2==0:
        m=(a/2)+((a/2)+1)
        
# mode