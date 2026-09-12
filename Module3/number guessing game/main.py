random_number = 27
attempts = 5
while attempts > 0:
    guess = int(input("whats your guess? "))
    attempts = attempts - 1
    if guess < 27:
        a = 27 - guess
        if a <= 1:
            print("hot")
        elif a <= 5:
            print("warm")
        elif a <= 10:
            print("cold")
        else:
            print("ice cold")
    if guess > 27:
        a = guess - 27
        if a <= 1:
            print("hot")
        elif a <= 5:
            print("warm")
        elif a <= 10:
            print("cold")
        else:
            print("ice cold")
    if guess == 27:
        print("congrats you were right")
        break
    else:
        print("you have", attempts, "left")
