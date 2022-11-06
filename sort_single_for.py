
givenList  =[2,0,1,2,1,0,1,2]
countList  =[0]*len(set(givenList))
sortedList =[]
for i in set(givenList):
    countList[i] = givenList.count(i)
for i in range(len(countList)):
    sortedList.extend([i]*countList[i])
print(sortedList)

# more good version


givenList  =[2,0,1,2,1,0,1,2,3,3,3,0,3,3]
sortedList =[]
for i in set(givenList):
    sortedList.extend( [i] * givenList.count(i) )
print(sortedList)
