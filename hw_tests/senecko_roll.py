import re
import random

def dice(dice_code):
    pattern = r'^(\d*)D(\d+)([+-]?\d+)?$'
    match = re.match(pattern, dice_code)

    if not match:
        return "Invalid dice code format."

    x = int(match.group(1)) if match.group(1) else 1
    y = int(match.group(2))
    z = int(match.group(3)) if match.group(3) else 0
    print("z: ", z)

    allowed_dice = [3, 4, 6, 8, 10, 12, 20, 100]

    if y not in allowed_dice:
        return f"Invalid dice type: D{y}. Only D3, D4, D6, D8, D10, D12, D20, D100 are allowed."

    rolls = [random.randint(1, y) for _ in range(x)]

    print("beforemodif: ", sum(rolls))
    total = sum(rolls) + z
    print("after: ", total)


    return f"Rolled {x}D{y} with a modifier of {z}: Rolls were {rolls}, Total is {total}."

examples = [
    dice("D3"),
    dice("D4"),
    dice("D6"),
    dice("D8"),
    dice("D10"),
    dice("D12"),
    dice("D20"),
    dice("D100"),
    dice("2D6"),
    dice("3D8+2"),
    dice("3D8-2"),
    dice("F5"),
    dice("2D7"),
    dice("4D6-2"),
]

for example in examples:
    print(example)