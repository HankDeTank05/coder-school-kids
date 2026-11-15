print ("Calculator")
choice = int(input("Enter an operation! (1 - add, 2 - subtract, 3 - multiply, 4 - divide, 5 - quit) " ))
while choice != 5:
    if(choice == 1 or choice == 2 or choice == 3 or choice == 4):
        number1 = int(input("What is the first number you are using? "))
        number2 = int(input("What is the second number you are using? "))
        if choice == 1:
            print (number1 , "+" , number2 , "=" , number1 + number2)
        elif choice == 2:
            print (number1 , "-" , number2 , "=" , number1 - number2)
        elif choice == 3:
            print (number1 , "x" , number2 , "=" , number1*number2)
        elif choice == 4:
            print (number1, "/" , number2 , "=" , number1/number2)
    else:
        print ("That is not a valid number, please enter another!")
    choice = int(input("Enter an operation! (1 - add, 2 - subtract, 3 - multiply, 4 - divide, 5 - quit) " ))
print ("Calculator powered off.")