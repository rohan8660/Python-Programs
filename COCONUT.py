t=int(input())
for i in range(t):
    a,b,c,d=list(map(int,input().split(" ")))
    retval=0
    if(c%a==0):
        retval+=c/a
    else:
        retval+=((c/a)+1)
    if(d%b==0):
        retval+=d/b
    else:
        retval+=((d/b)+1)
    print(int(retval))
