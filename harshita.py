n= input1
x= input2
ls=input3
count=0
for i in range(len(ls)):
    j=0
    flag=0
    if(ls[i]==-1):
        break
    b=i
    while(j<x):
        j+=1
        b=ls[b]
        if(b<n):
            continue
        else:
            flag=1
    if(flag==0):
        count+=1
return( count )
