import math

while True:
  print("Welcome to my area and perimeter calculator!")
  print("")
  print("Input 1 for rectangle.")
  print("Input 2 for triangle.")
  print("Input 3 for circle.")
  print("Input 4 for trapezoid.")
  print(" ")
  choice = int(input("Please input which shape area you would like to find: "))
  print(" ")

  if choice == 1:
    rect_width = float(input("Please input the width of your rectangle: "))
    rect_length = float(input("Please input the length of your rectangle: "))
    print(" ")
    print("Your rectangle has an area of", rect_width * rect_length,
          "units, and a perimeter of",
          rect_width + rect_width + rect_length + rect_length, "units.")
    print(" ")
    print(" ")

  elif choice == 2:
    tri_base = float(input("Please input the base of your triangle: "))
    tri_height = float(input("Please input the height of your triangle: "))
    print(" ")
    print("Your triangle has an area of", tri_base * tri_height / 2, "units.")
    print(" ")
    print(" ")

  elif choice == 3:
    circ_rad = float(input("Please input the radius of your circle: "))
    print("Your circle has an area of", math.pi * circ_rad * circ_rad,
          "units.")
    print(" ")
    print(" ")

  elif choice == 4:
    trap_base_1 = float(input("Please input base 1 of the trapezoid: "))
    trap_base_2 = float(input("Please input base 2 of the trapezoid: "))
    trap_height = float(input("Please input the height of the trapezoid: "))
    print(" ")
    print("Your trapezoid has an area of",
          (trap_base_1 + trap_base_2) / 2 * trap_height, "units.") 
    print(" ")
    print(" ")

  else:
    print("Oops, you messed up. That is wrong. ):")
    print(" ")
    print(" ")
    print(" ")
