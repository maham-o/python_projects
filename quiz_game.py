print("Welcome to my computer quiz!")
playing = input("Do you want to play?").lower().strip()
if playing != 'yes':
    quit()
score = 0
print("Okay! Let's play.")
answer = input("What does CPU stand for? ").lower().strip()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ").lower().strip()
if answer == "random access memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower().strip()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower().strip()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")