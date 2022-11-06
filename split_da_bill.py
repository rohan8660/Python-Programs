n,i,j=list(map(int,input().split()))
i=i-1
j=j-1
ls=list(map(int,input().split()))

a=0
a+=ls[i]

b=0
b+=ls[j]
sum=0
for x in range(len(ls)):
    if(x!=i and x!=j):
        sum+=ls[x]
a+=sum//2
b+=sum//2
print(a, end=" ")
print(b)
