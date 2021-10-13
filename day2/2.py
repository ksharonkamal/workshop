#accept a string from user and count the number of vowels in it

vowels = ['a','e','i','o','u']
str = input("enter a string : ")
cnt = 0

for i in str:
    if i in vowels:
        cnt+=1

print("The number of vowels are :",cnt)