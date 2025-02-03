def chessboard(n=8):
    for i in range(n):
        if i % 2 == 0:
            print(int(n/2)*"# ")
        else:
            print(int(n/2)*" #")
    return

print(chessboard(7))