from itertools import permutations ,combinations,combinations_with_replacement
from functools import reduce
n,M=[int(i) for i in input().split(" ") ]
tot=0

for i in range(2**M):
    for j in range(2**M):
        if(j&i==0):
            tot+=1
print(tot)


# ls=[]
# k=permutations(range((2**M)),n)
# s=combinations_with_replacement(range(2**M), n)
# for i in k:
#     ls.append(i)
# for i in s:
#     ls.append(i)
# ls=list(set(ls))
# ls.sort()
# lss=[]
# for i in ls:
#     ad=reduce((lambda x,y:x&y),i)
#     if(ad==0):
#         lss.append(i)    
# print((lss))