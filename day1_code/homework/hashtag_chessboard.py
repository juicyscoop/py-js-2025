
def chessboard(n=8):
    result = ""
    for i in range(n):
        if i % 2 == 0:
            # radek zaciname hashtagem
            for ii in range(n):
                if ii % 2 == 0:
                    result += "#"
                else:
                    result += " "
        else:
            # radek zaciname mezerou
            for ii in range(n):
                if ii % 2 == 0:
                    result += " "
                else:
                    result += "#"
        result += "\n"
    return result

c = chessboard(7)
print(c)
