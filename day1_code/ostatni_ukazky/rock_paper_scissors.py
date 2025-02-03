# 1 = Rock
# 2 = Paper
# 3 = Scissors
from random import randint as ri

{
    "Rock": {
        "beats": ["Scissors"],
        "loses": ["Paper"]
    },
    "Paper": 2,
    "Scissors": 3
}

computer_input = ri(1, 3)

user_input = input("Enter a number: 1,2,3 \n")

user_input_integer = int(user_input)

print("Computer chose: ", computer_input)

if user_input_integer not in [1,2,3]:
    print("Invalid input")
else:
    if user_input_integer == computer_input:
        print("Draw")
    if user_input_integer == 1:
        if computer_input == 2:
            print("Computer wins, you lose!")
        elif computer_input == 3:
            print("Computer loses, you win!")
    if user_input_integer == 2:
        if computer_input == 1:
            print("Computer loses, you win!")
        elif computer_input == 3:
            print("Computer wins, you lose!")
    if user_input_integer == 3:
        if computer_input == 1:
            print("Computer wins, you lose!")
        elif computer_input == 2:
            print("Computer loses, you win!")

print("Game finished...")




