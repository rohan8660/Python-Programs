def transpose(m):
    rows=len(m)
    cols=len(m[0])
    tm=[[0 for x in range (rows)] for y in range (cols)]
    for i in range(cols):
        for j in range(rows):
            tm[i][j]=m[j][i]
    print (tm)

    
    
