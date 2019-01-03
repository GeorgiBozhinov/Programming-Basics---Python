product = input()
city = input()
quantity = float(input())

dict_sofia = {'coffee': 0.50, 'water': 0.80, 'beer': 1.20, 'sweets': 1.45, 'peanuts': 1.60}
dict_plovdiv = {'coffee': 0.40, 'water': 0.70, 'beer': 1.15, 'sweets': 1.30, 'peanuts': 1.50}
dict_varna = {'coffee': 0.45, 'water': 0.70, 'beer': 1.10, 'sweets': 1.35, 'peanuts': 1.55}

price = 0
if city == "Sofia":
    for key, value in dict_sofia.items():
        if key == product:
            price += quantity * value
elif city == "Plovdiv":
    for key, value in dict_plovdiv.items():
        if key == product:
            price += quantity * value
else:
    for key, value in dict_varna.items():
        if key == product:
            price += quantity * value

print(price)


