import random

while True:
    number = input("Type a number: ")
    if number.isdigit():
        number = int(number)
        if 0 <= number <= 100:
            break
    else:
        print("Incorrect input")
        continue

random_number = random.randrange(number)

attempts = 5
i = 0
while i < attempts:
    guess = input("Type your guess: ")
    i += 1
    if guess.isdigit():
        guess = int(guess)
        if guess == random_number:
            print(f"Correct, after {i} attempt/s")
            quit()
        elif guess > random_number:
            print("your guess is higher than our number!")
            continue
        else:
            print("your guess is smaller than our number!")
            continue
    else:
        print("Incorrect input, try again!")
        continue

print("You Failed !")



