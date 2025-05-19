import random

al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" ,"z"]
yourWord = []
count = 0 # 

length = int(input("how long is your word? "))
for letter in range(length):
  yourWord.append("")

while True:
  guess = random.choice(al)
  response = input(f"Is there {guess} in your word? ")
  
  if response == "y":
    location = int(input(f"Enter the location of each letter {guess} in your word. "))
    yourWord[location] = guess
    count += 1
    print(*yourWord)
    
  if response == "n":
    al.remove(guess)

  if count == len(yourWord):
    print (f'your word is {"".join(str(x) for x in yourWord)}!!')