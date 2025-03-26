from random import randint

def guessing_game():
    random_number= randint(0, 100)


    while True:
        try:
            user_guess = int(input("Guess the number:"))

            if user_guess < random_number:
                print ("Too small!")
            elif user_guess > random_number:
                print ("Too big!")
            else:
                print("Congratulations! You won")
                break

        except ValueError:
            print("It's not a number!")

guessing_game()