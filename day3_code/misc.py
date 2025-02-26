# cislo
a = input("Zadej cele cislo:")

try:
    cislo = int(a)
    print(f"cislo: {cislo}")
except ValueError as e:
    err_msg = f"Nezadal si validni cele cislo!: {e.args}"
    raise ValueError(err_msg)





"""
except IndexError as ix:
    print("index is wrong!")
finally:
    print("I get executed always!")
"""
