# Create a variable with the name "my_list"
# The type of this variable is: a lsit of strings
#This variable is being initialized as an empty list
my_list = []

print(my_list) #pritns the whole list

my_list.append("first") #Append means to add to the end of list
print(my_list[0]) #It then prints the first entry in the list

print(my_list)

#  The index at which to insert the item
#              |        The item to be inserted
#              v  vvvvvv
my_list.insert(0, "zero") # we are inserting the string "zero" at index 0
print(my_list)

my_list.remove("zero") #Removing an item from the list, equal to the string: "zero"
print(my_list)

my_list.append("third")
print(my_list)

my_list.insert(1, "second") #We are adding the word "second" in between what we already have put down: first and third
print(my_list)

#Printing out what is in the list one entry per line, rather then all on the same line
print(my_list[0])
print(my_list[1])
print(my_list[2])

# TODO come back and explain what these are and how they work

print("Keyword for loop")
for item in my_list:
    print(item)

print("Index based for loop")
for i in range(len(my_list)):
    print(my_list[i])

'''
for i in range(12):
    print(i)
'''
'''
print(len(my_list)) #Len gets the length of a list
my_list.append("fourth")
print(len(my_list))
'''

#Range function takes a single numer and returns...
#  a sequence of numbers starting with zero
# and ending in the number you give - 1
'''
for i in range(3): 
    print(my_list[i])
'''

#The code is making a sequence of numbers that starts at 10 and then counts adds by -1, going to 1.
# It then prints the sequence of numbers in the range, prints them one number per line
'''
for num in range(10, 0, -1):
    print(num)
'''

#It generates a sequence of numbers containing multiples of 3 going up to 30
#It prints a single multiple per line 
'''
for num in range(3, 31, 3):
    print(num)
'''

'''
print("Fibonacci Sequence - while-loop implementation")

stop_at = 10
current_n = 2
fw = [0, 1]
while current_n <= stop_at:
    print(current_n)
    next_val_in_seq = fw[current_n-1] + fw[current_n-2]
    fw.append(next_val_in_seq)
    print(fw)
    current_n = current_n + 1

print("Fibonacci Sequence - for-loop implementation")

ff = [0, 1]
for n in range(2, 11, 1):
    print(n)
    k = ff[n-1] + ff[n-2]
    ff.append(k)
    print(ff)
'''

for i in range(1, 6):
    print(i)

