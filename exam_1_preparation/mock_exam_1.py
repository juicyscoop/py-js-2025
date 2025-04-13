

def shorten(text_retezec):
    # Rozdelit ten textovy retezec na slova - pomoci mezer
    rozdeleny_retezec = text_retezec.split() # Mezera je default ni separator
    print(f"rozdeleny_retezec: {rozdeleny_retezec}")
    
    # pro kazde slovo = vzit prvni pismeno a kapitalizovat
    output = []
    for slovo in rozdeleny_retezec:
        prvni_pismeno_velkym = slovo[0].capitalize()

        output.append(prvni_pismeno_velkym)

    return "".join(output)


print(shorten("A long time ago, in a galaxy far, far away..."))