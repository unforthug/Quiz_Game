

print("Welcome to my computer quiz!")

while True:
    playing = input("Do you want to play the game ? (yes/no) ")

    if playing.lower() == "yes":
        break
    elif playing.lower() == "no":
        quit()
    else:
        "Your answer is not clear, Please repeat"
        playing = input("Do you want to play the game ? (yes/no) ")

print("Okey! Let's Play! ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unis":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory ":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"Your Score is {score}")
print(f"Your Score is {(score/4) * 100} %")

