from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    str_num = input("Enter number:")

    try:
        num = int(str_num)
    except ValueError:
        print(f"You did not enter a number! You entered: {str_num}")
        continue
    finally:
        print("I always get executed!")

    if num == rnd:
        print("Great!")
        guessed = True
    else:
        print("Wrong!")