

def bubbleSort(ls):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if(ls[i]>ls[j]):
                ls[i],ls[j]=ls[j],ls[i]
    return(ls)

ls=[1,3,7,9,2]
ls=bubbleSort(ls)
print(ls)