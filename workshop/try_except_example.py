cisla_od_uzivatele = []

class DuplicateError(Exception):
    pass

while len(cisla_od_uzivatele) < 6:
    try:
        cislo = input("Zadej cislo:")
        try:
            cislo = int(cislo)
        except ValueError:
            print("To neni validni cislo, zkus to znovu!")
            continue

        if cislo in cisla_od_uzivatele:
            raise DuplicateError("Duplicate!")

        if cislo > 49 or cislo < 1:
            print("Zdaej cislo v intervalu <1;49>!")
            continue

        cisla_od_uzivatele.append(cislo)
    
    except DuplicateError:
        print("Cislo je duplikatni!")
        continue


