def printR():
    # # first three lines
    # for i in range(1,4):
    #     print()
    #     for j in range(i*2):
    #         print("*",end="")

    # # next three lines
    # for i in range(4,1,-1):
    #     print()
    #     for j in range(i*2):
    #         print("*",end="")
    # print()
##
    for i in range(1,8):
        
        if(i==1):
            print("**",end="")
            for j in range(2):
                print("**")
        # print("-",end="")
        if(2<=i<5):
            print("**",end="")
            for j in range(0,i):
                print(" ",end="")
            print("**")
        
        # elif(i<=8):
            # for j in range(int(i/2),0,-1):
            #     print(" ",end="")
            # print("**")
 
##
    # next six lines
    for i in range(1,8):
        if(i<2):
            for j in range(i*2 -2):
                print("*",end="")
        else:
            print("**",end="")
            for j in range(int(i-2)):
                print(" ",end="")
            print("**")
    print()
    print()
printR()