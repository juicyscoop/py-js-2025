def calculate_net(gross, tax):
    return gross*(1-tax)

a = 10**5
print(calculate_net(a, 0.15))