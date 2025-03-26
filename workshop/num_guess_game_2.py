import random

# Inicialiace
spodni_limit = 1
horni_limit = 1000
pokusy = 10
cislo_pokusu = 0

VYHRA = 10
print(f"vyhra: {VYHRA}")

while True:
    if cislo_pokusu > pokusy:
        print("Prohrál jsi!", "Konec hry!")
        break
    
    pocitac_hada = random.randint(spodni_limit, horni_limit)
    if pocitac_hada == VYHRA:
        print("Vyhrál jsi!", "Konec hry!")
        break
    
    print(f"pocital zkusil: {pocitac_hada}")
    rada = input("Zadej v/m")
    if rada == "v":
        horni_limit = pocitac_hada - 1
    elif rada == "m":
        spodni_limit = pocitac_hada + 1

    cislo_pokusu += 1
