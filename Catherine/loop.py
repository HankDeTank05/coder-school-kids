num = int(input("Pick a number! "))
times = 0
while num != 1:
    print(num)
    if num%2 == 0:
        num = num/2
    elif num%2 != 0:
        num = num*3
        num = num+1
    times = times + 1
print ("Your number has reached 1! It took " , times , "changes!")