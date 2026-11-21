password = input("Enter your password! ")
has_number = False
has_special = False
for letter in password:
    if letter == "@":
        has_special = True
    if letter == "!":
        has_special = True
    if letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9" or letter == "0":
        has_number = True
if has_special and has_number:
    print ("'", password ,"' Is a strong password!")
elif has_special or has_number:
        print ("'", password ,"' Is an okay password.")
else:
     print ("'", password ,"' Is a weak password.")