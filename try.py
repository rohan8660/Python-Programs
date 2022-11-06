
# cricket score

def lastLegalBall(ls,i):
    for j in range(i,-1,-1):
        if(ls[j]!=-1):
            return ls[j]

ls=A
if(ls[0]==-1):
    score=6
else:
    score=ls[0]
for i in range(1,len(ls)):
    if (ls[i]==-1):
        score+=lastLegalBall(ls,i)
        ls[i-1]=-1
    else:
        score+=ls[i]
    return(score)



# sub array product


def countSubArrayWithOddProduct(A, N):
    count = 0
    last = -1
    K = 0
    for i in range(N):
        if (A[i] % 2 == 0):
            K = (i - last - 1)
            count += (K * (K + 1) / 2)
            last = i
    K = (N - last - 1)
 
    count += (K * (K + 1) / 2)
    return count




    #third answer
t=int(input())
for i in range(t):
    n=int(input())
    k=int(input())
    x=int(input())
    ls=set(list(map(int,input().split())))
    print((len(ls)-k)*x)