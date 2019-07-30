import random
# a = [5,6,7,8,random.randint(0,20)]
# b = []
# for x in range(1,10):
#     print(x)
#     b.append(x*2)
# print(a)
# print(b)

a = []
for i in range (4):
    #1) generate a random number and 2) append it to a 
    randomNumber = random.randint(0,20)
    # print(randomNumber)
    a.append(randomNumber)
    # print(a)

print(a)

# 3) calculate the sum of each item in a

sum = 0
# sum = sum+3 # new sum 3
# sum = sum+15 # new sum 3
# sum = sum+10 # new sum 3
# sum = sum+9 # new sum 3

for i in a:
    print("i is: ", str(i))
    sum = sum+i 
    print("current sum is: " , str(sum))

print("final sum" , str(sum))
