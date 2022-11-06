t=int(input())
for i in range(t):
    n=int(input())
    s=(input())
    print("Case #"+str(i+1)+": ",end="")
    for j in range(len(s)):
        c=s[j]
        k=j
        ans=1
        while(ord(c)>ord(s[k-1])):
            if(k==-1):
                break
            ans+=1
            k-=1
            c=s[k]
            
        print(ans,end=" ")
    print()
