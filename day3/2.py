#program to sum all items in dictionary

dict1 = {"tony" : 100 , "thor" : 200 , "peter" : 300 ,"strange" : 400}
sum = 0

# for i in dict1.values():
#     sum+=i

for i in dict1:
    sum+=dict1[i]

print("sum of items in dict1 is ",sum)
