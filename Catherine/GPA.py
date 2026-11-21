# total = 0
# math = input("Enter your semester grade for math! ")
# english = input("Enter your semester grade for ELA! ")
# science = input("Enter your semester grade for science! ")
# ss = input("Enter your semester grade for social studies! ")
# if math == "A":
#     total = total + 4
# if english == "A":
#     total = total + 4
# if science == "A":
#     total = total + 4
# if ss == "A":
#     total = total + 4
# if math == "B":
#     total = total + 3
# if english == "B":
#     total = total + 3
# if science == "B":
#     total = total + 3
# if ss == "B":
#     total = total + 3
# if math == "C":
#     total = total + 2
# if english == "C":
#     total = total + 2
# if science == "C":
#     total = total + 2
# if ss == "C":
#     total = total + 2
# if math == "D":
#     total = total + 1
# if english == "D":
#     total = total + 1
# if science == "D":
#     total = total + 1
# if ss == "D":
#     total = total + 1
# if math == "F":
#     total = total
# if english == "F":
#     total = total
# if science == "F":
#     total = total
# if ss == "F":
#     total = total
# average = total/4
# print ("Your GPA is" , average , "!")


total = 0
choice = int(input("Enter the number of classes you take! "))
for i in range (0, choice):
    if i == 0:
        grade = int(input("Enter your grade percentage for your first class! "))
    else:
        grade = int(input("Enter your grade percentage for your next class! "))
    total = grade + total
print ("Your percent GPA is" , total/choice , "!")