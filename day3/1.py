#program to check if all items in tuple are same

tuple1 = (45,45,45,45,3)
n1 = tuple1[0]
flag = 0
for i in tuple1:
    if n1 != i:
        print("elemets in tuple are different!")
        flag=1
        break

if flag == 0:
    print("elements in tuple are same!")