print("Welcome To The Quiz! ")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
  quit()

print("Yes, Lets play!")
score = 0
answer = input("How many time zones does Russisa have? ")
if answer.lower() == "11":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input("What's the national flower of Japan? ")
if answer.lower() == 'cherry blossom':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("How many sreipes are there on the U.S. flag? ")
if answer.lower() == '13':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What's the national animal of Australia? ")
if answer.lower() == 'red kangaroo':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("How many days does it take for the Earth to orbit the sun? ")
if answer.lower() == '365':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What's the capital of Canada? ")
if answer.lower() == 'ottawa':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("You got " + str(score) + "question correct!")
print("You got " + str((score / 6) * 100) + "%")
