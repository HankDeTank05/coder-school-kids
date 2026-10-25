# num = int(input ("Choose a number! "))
# count = 1
# while count <= 12:
#     print (num , "x", count , "=", num*count ,)
#     count = count + 1


# age = int(input ("Enter your age! "))
# while age < 0:
#     print ("Please enter a positive number! ")
#     age = int(input ("Enter your age! "))


# num = 0
# while num <= 100:
#     if num % 2 == 0:
#         print (num)
#     num = num + 1


# num = int(input("Choose a number! "))
# count = 1
# total = 0
# while count <= num:
#     total = count + total
#     count = count + 1
# print (total)


# choice = int(input("Guess my number! "))
# num = 83
# while choice != num:
#     print ("That's not right!")
#     if choice > num:
#         print ("That was too high. Try again! ")
#     if choice < num:
#         print ("That was too low. Try again! ")
#     choice = int(input("Guess my number! "))
# print ("That's right!")


# for i in range(0, 11, 2):
#     print (i)


# num = int(input("Choose a number!" ))
# for i in range (1, 13):
#     print (num , "x", i , "=", num*i,)


# for i in range (10, 0, -1):
#     print (i)


# for i in range (1, 20, 2):
#     print (i)


# word = input("Enter a word!" )
# for letter in word:
#     print (letter)


# num = int(input("Choose a number!"))
# total = 0
# for i in range (1, num + 1):
#     total = total + i
# print (total)


word = input("Enter a word! ")
reverse_word = ""
for letter in word:
    reverse_word = letter + reverse_word
print (reverse_word)