import random

times = 0
num = 0
while num != 6:
    num=random.randint(1,6)
    print ("You rolled a",num,"!")
    times += 1
print ("It took" , times , "rolls to roll a 6!")



# print(random.randint(1,6))