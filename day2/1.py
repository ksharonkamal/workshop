#program to separate positive and negative numbers into two separate lists

numlist = [1,3,4,-3,2,-7,5,-12,-6,-5,9]
positivelist=list()
negativelist=list()

for i in numlist:
    if i>=0:
        positivelist.append(i)
    else:
        negativelist.append(i)

print("Positive number list is ", positivelist)
print("Negative  number list is ", negativelist)
