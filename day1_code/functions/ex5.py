#      (F - 32) * 5
# C =  ------------
#           9


def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

fahrrenheit_temp = 100
celsius_temp = convert_to_celsius(fahrrenheit_temp)

print(celsius_temp)