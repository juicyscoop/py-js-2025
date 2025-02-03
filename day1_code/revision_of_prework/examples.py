def create_christmas_tree(height=None):
    if height is None:
        return
    for i in range(height):
        for _ in range(i + 1):
            print("*", end="")
        print()

create_christmas_tree()






