
marker_x = "x"
marker_o = "o"
playing = True
my_tern

while playing:

    choice = input('choose a spot ')

    column_number = int(choice[0])
    row_number = int(choice[2])
    
    left_number_is_ok = column_number == 0 or column_number == 1 or column_number == 2
    right_number_is_ok = row_number == 0 or row_number == 1 or row_number == 2
    if len(choice) == 3 and choice[1] == " " and  right_number_is_ok and left_number_is_ok:
        # process the string into row and column number
        print("good")
    else:
        print("bad")
        break

    print("  0   1   2")
    print("0 * | * | * ")
    print(" ---+---+---")
    print("1 * | * | * ")
    print(" ---+---+---")
    print("2 * | * | * ")

