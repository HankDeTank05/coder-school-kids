# for i in range (1, 11):
#     print (i)


# for i in range (50, 0, -5):
#     print (i)


# answer = 0
# num = int(input("Choose a number! "))
# for i in range (0, num, 3):
#     if i%2 == 0:
#         answer = answer + i
# print (answer)

# num = int(input("Choose a number! "))
# for i in range (1, 13):
#     print (num , "x" , i , "=" , num*i)

# answer = 1
# num = int(input("Choose a number! "))
# for i in range (num, 1, -1):
#     answer = answer*i
# print (answer)


word = input("Pick a word! ")
count = 0
for letter in word:
    if letter == ("a"):
        count = count + 1
    if letter == ("e"):
        count = count + 1
    if letter == ("i"):
        count = count + 1
    if letter == ("o"):
        count = count + 1
    if letter == ("u"):
        count = count + 1
print (count)