#program to print the following series where N should be taken as input
# 21,32,54,87,131,186,.....N

# Differences are multiples of 11 starting from 11
# 21 + 11×1 = 32
# 32 + 11×2 = 54
# 54 + 11×3 = 87
# 87 + 11×4 = 131
# 131 + 11×5 = 186

series = [ ]
start = 21
N = int(input("enter he ending range : "))

for i in range(N+1):
    start = start + 11 * i
    series.append(start)

print("the series is : ", series)

