
def dogs_age(age):
    # Pro prvni dva roky je jeden psi rok 10.5 lidskych let
    # Pro vsechny nalsedujici roky je jeden psi rok 4 lidske roky
    if age > 2:
        print(10.5 * 2 + (age - 2) * 4)
        return None
    print(10.5 * age)
    return




dog_age_human_years = 10

calculated = dogs_age(dog_age_human_years)

print(f"Dog age in human years is {dog_age_human_years}.")
print(f"Dog age in dog years is {calculated}")