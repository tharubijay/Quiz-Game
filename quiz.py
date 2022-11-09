print("Hello Bijay Welcome to my Game Zone")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Do you like ice-cream ? ")
if answer.lower() == "yes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Do you play cricket ? ")
if answer.lower() == "yes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Do you like football ? ")
if answer.lower() == "no":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("CPU stands for: ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")