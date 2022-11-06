t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    ls.sort()
    x=1
    se=set(ls)
    se=list(se)
    se.sort()
    print(type(se))
    tot=0
    print(ls)
    for i in se:
        tot=tot+(ls.count(i)*x)
        x+=1
    print(tot)
