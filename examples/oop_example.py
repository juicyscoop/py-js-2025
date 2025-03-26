def a():
    return "A"


reference = a
print(f"reference: {reference}") 


hodnota = a()
print(f"hodnota: {hodnota}") 


class Pes:
    vek = 24
    jmeno = "Pes"
    vaha = 80

p_instance = Pes()
print("instance:", p_instance)
print("instance:", p_instance.vek)
print("instance:", p_instance.vaha)


p_reference = Pes
print("reference:", p_reference)
print("reference:", p_reference.vek)
print("reference:", p_reference.vaha)

p_instance_2 = p_reference()
print("instance 2 :", p_instance_2)
print("instance 2:", p_instance_2.vek)
print("instance 2:", p_instance_2.vaha)


# p2 = Pes()
# print(p2.vek)

# print(p == p2)
