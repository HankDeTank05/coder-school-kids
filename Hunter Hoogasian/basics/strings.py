#String Variable
#vvvvvvvv
first_name = "Hunter"
#             ^^^^^^
#       String literal
last_name = "Hoogasian"

print(first_name, last_name)

# You can contatenate two variables with an addition sign
full_name_concat = first_name + " " + last_name

print(full_name_concat)

# 0         1
# 0123456789012345
# Hunter Hoogasian

# you can slice strings by putting square brackes after the string. inside the square brackets, there are tow numbers that are seperatted by a :
#To the left of the : is the starting index and the number on the right is the index of the last charcter plus one

first_name_slice = full_name_concat[0:6]
print(first_name_slice)
last_name_slice = full_name_concat[7:16]
print(last_name_slice)

print(full_name_concat[0:6] == full_name_concat[:6]) # this evaluates to true
print(full_name_concat[7:16] == full_name_concat[7:]) # this evaluates to true

#Your allowed to not use the starting index if your slice starts at the beginning (0)
#Your allowed to not se the ending index if your slice ends at the end of the string being sliced

#        0         1
#        01234567890123456789
alpha = "AaBbCcDdEeFfGg"
capitals = alpha[0:13:2]
print(capitals)
lowers = alpha[1:14:2]
print(lowers)

# The third optional number that you are allowed to include in the slice is the step, which is how much to count by
# for example, on line 36, alpha is slcied using hte following index numbers: 0 2 4 6 8 10 12 

#Format String
full_name_format = f"{first_name} {last_name}"
print(full_name_format)

x_pos = 247
y_pos = 771
coords = f"({x_pos}, {y_pos})"
print(coords)

# Format string
print(f"My name is {first_name}")

# response_name = input("What is your name? ")
# response_quest = input("What is your quest? ")
# response_color = input("What is your favorite color? ")
# print(f"Your name is {response_name}. Your quest is supposedly {response_quest}. And your favorite color is {response_color}")
# if response_color.lower() != "blue":
#     print("You shall not pass")
# else:
#     print("Please proceed")

# The lower function replaces letter in the string with their lower case versions
# the upper function does the reverse

quote = "\"Do or do not, there is no try\" - Yoda" # Escaoe charcter for qoutews within a string
new_line = f"{first_name}\n{last_name}"
print(new_line)
full_name_tab = f"{first_name}\t{last_name}"
print(full_name_tab)