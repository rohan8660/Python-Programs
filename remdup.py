
def remdup(l):
    dupr=[]
    for i in l:
        if i not in dupr:
            dupr.append(i)
    l=dupr
    print(l)
