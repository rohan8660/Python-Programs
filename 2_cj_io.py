t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    res="A"
    lst=65
    alt=0
    
    for j in range(len(ls)):

        if(alt==0):
            if((ls[j]!=ls[-1])):
                n=ls[j+1]
                for k in range(ls[j]):
                    lst+=1
                    res+=(chr(lst))
                if(ord(res[-1])+(65+n-ord(res[-1]))>ord(res[-1])):
                    res=res[:-1]+chr(ord(res[-1])+(65+n-ord(res[-1])))
                alt=1
            else:
                n=ord(res[-1])
                for k in range(ls[j]):
                    n=n+1
                    res+=chr(n)
            
        else:
            for k in range(ls[j]):
                lst-=1
                if((ls[j]==ls[-1])):
                    res+=(chr(64+(ls[j])-k))
                else:
                    lst=ord(res[-1])
                    res+=(chr(lst-1))
                    lst-=1
            alt=0
    print("Case #"+str(i+1)+": " +res)

