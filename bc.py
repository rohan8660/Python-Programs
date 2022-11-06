t=int(input())
ls=[]
for j in range(t):
    D,d,P,Q=[int(k) for k in input().split(" ")]

    # x=D//d
    # r=D-d*x
    x,r=list(divmod(D, d))

    
    ret = r*(P+(x*Q))
    for i in range(x):
        ret += d*(P+(i*Q))
    ls.append(ret)
for i in ls:
    print(i)