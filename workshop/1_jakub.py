from random import randint

computer_guess = randint(1, 100)

while True:
    try:
        player_guess = (input("Guess the number:"))
        number = int(player_guess)
    except ValueError:
        print("Its not a number!")
        continue
    if number < computer_guess:
        print("too small")
    elif number > computer_guess:
        print("too big")
    else:
        print("you win")
        break