a=0
m,n=list(map(int,input().split()))
no=0
while(m>=n):
    m=m-n
    a=a+1
    no+=a
    
print(no)
    
