# 1. Print all integers form 0 to 150
for x in range (0,151,1):
    print(x)

# 2. Print all multiples of 5 from 5 to 1,000
num = 5
while num < 1001:
    if num % 5 == 0:
        print (num)
    num = num + 1

# 3. Count Dojo
for x in range (1, 101, 1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# 4. Print sum of first odd 500,000 numbers
sum = 0
# counter = 0
# while counter < 500001:
#     if counter % 2 == 1:
#         sum += counter
#     counter+=1
for x in range (1,500000,2):
        sum += x
print(sum)

# 5. countdown by 4
for x in range (2018, 0, -4):
    print(x)

# 6. flex counter
lowNum = 1
highNum = 100
mult = 4
for x in range (lowNum, highNum, 1):
    if x % mult == 0:
        print(x)
