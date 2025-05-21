dictionary = {} #Empty dic

# Putting stuff into an existing dictionary
#          Keys           Values
#          vvvvvvv    vvvvvvvvvvvv
dictionary["Apple"] = "A red fruit"
dictionary["Microsoft"] = "Company"

key_math = "MATH"
key_english = "ENGLISH"
key_history = "HISTORY"
grades = {
    key_math: 94.7,  # This is a key/value pair
    key_english: 18.9,
    key_history: 100
}

'''
what is the difference between a dictionary and a list?
specifically...
which one is squential and which one is not?
List is squential and dicotionary is not 

how are individual values in lists and dictionaries referenced?
lists: my_list[7] <- this one uses an index number
dicts: my_dict["key"] <- this one uses a key (does not have to be string, but usually is)

'''

print(grades) # Prints out the key value pairs in the dictionary
print(key_math) # Prints out a specfic key in the dictionary
print(grades[key_math]) # Prints out the grade for math (we use the stirng "MATH" to access that value)

print(grades.keys()) # Prints out all of the keys in a single line
print(grades.values()) # Prints out all of the values in a single line

# We want to print out each key in grades on its own line
for key in grades.keys():
    print(key)

#printing out each value in grades on its own line
for value in grades.values():
    print(value)

# come back once you've learned strings and functions, and write a function that prints a nicely formatted dictionary

def print_dict(dict_2_print: dict[any, any]) -> None:
    print("print_dict function output:")
    for key in dict_2_print.keys():
        print(key, end=": ")
        print(dict_2_print[key])

print()
print_dict(grades)