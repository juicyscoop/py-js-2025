import random

mozne_hody = (
    "D100",
    "D20",
    "D12"
    "D10",
    "D8",
    "D6",
    "D4",
    "D3",
)

def roll_dice(dice_code):
    for dice in mozne_hody:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
            except ValueError:
                return "Invalid input"
            dice_value = int(dice[1:])
            break
    else:
        return "Invalid input"
    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Invalid input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Invalid input"

    return sum ([random.randint(1, dice_value) for _ in range(multiply)])+ modifier


if __name__ == "__main__":
    print(roll_dice("D10"))
    print(roll_dice("2D3"))
    print(roll_dice("XD20"))
    print(roll_dice("XD20"))
    print(roll_dice("XD20"))
    print(roll_dice("XD20"))
    print(roll_dice("XD20"))
    print(roll_dice("XD20"))