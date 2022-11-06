input1=5
input2=[1,1,2,3,5]

if(len(input2)<3):
    return -999
if(input2[-1]-input2[-2]==input2[-2]-input2[-3]):
    return input2[-1]+input2[-1]-input2[-2]
if(input2[-1]/input2[-2]==input2[-2]/input2[-3]):
    return input2[-1]*(input2[-1]/input2[-2])
if (input2[-1]==input2[-2]+input2[-3] ):
    return input2[-2]+input2[-1]
else:
    return -999
