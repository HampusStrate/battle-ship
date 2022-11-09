print("Welcome to the software programming quiz")

playing = input("Do you want to play the quiz? ")
name = input()

if playing.lower() != "yes":
    quit()

print("Let's start the game!")
score = 0

answer = input("What does HTML stand for? ")
if answer == "hypertext markup language":
    print("Correct!!")
    score += 1
else:
    print("Wrong answer!")

answer = input("What does CSS stand for? ")
if answer == "cascading style sheets":
    print("Correct!!")
    score += 1
else:
    print("Wrong answer!")

answer = input("What does JS stand for? ")
if answer == "javascript":
    print("Correct!!")
    score += 1
else:
    print("Wrong answer!")

print("Your score is " + str(score))
print("You got " + str(score / 4) + "%.")