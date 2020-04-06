#number guessing game
win_number=12
guess_number=int(input("guess any number between 1 and 20\n"))

if guess_number==win_number:
    print("YOU WIN!!")
else:
    if guess_number<win_number:
        print("too low")
    else:
        print("too high")
