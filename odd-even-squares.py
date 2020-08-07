def sumsquare(l):
    odd=[]
    even=[]
    final=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    evensum=0
    oddsum=0
    for i in odd:
        oddsum=oddsum+(i*i)
    for i in even:
        evensum=evensum+(i*i)
    final.append(oddsum)
    final.append(evensum)
    print(final)
