name: str = "Hunter" # String variable
age: int = 17 # Int 
can_drive: bool = None # None makes the variable have no value or makes equal to nothing

if age > 15: 
    can_drive = True
else:
    can_drive = False

# Create a variable with the name "my_list"
# The type of this variable is: a lsit of strings
#This variable is being initialized as an empty list
my_list: list[str] = []

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

for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(my_list[i])



