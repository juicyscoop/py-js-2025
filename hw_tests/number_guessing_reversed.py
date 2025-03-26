from random import randint

def user_input():
    options = ["too low", "too high", "you win"]
    while True:
        user_choice = input().lower()
        if user_choice in options:
            return user_choice
        print ("Invalid input. Please try again.")


def main():
    print(f"Think about a number from 0 to 1000 and let me guess it!")
    print(f"Press enter to continue...")
    input ()
    min_range = 0
    max_range = 1000
    user_guess = ""

    while user_guess != "you win":
        guess = (max_range - min_range) //2 + min_range
        print (f"Your number is {guess}")

        user_guess = user_input()

        if user_guess == "too high":
            max_range = guess
        elif user_guess == "too low":
            min_range = guess
    print(f"I won!")

if __name__ == "__main__":
    main()