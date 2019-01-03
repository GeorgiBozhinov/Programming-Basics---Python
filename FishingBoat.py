budget = int(input())
season = input()
people = int(input())

price = 0
discount = 0.0

if season == "Spring":
    price = 3000

    if people <= 6:
        discount += 0.1
    elif 7 <= people <= 11:
        discount += 0.15
    elif 11 < people <= 18:
        discount += 0.25

elif season == "Summer":
    price = 4200

    if people <= 6:
        discount += 0.1
    elif 7 <= people <= 11:
        discount += 0.15
    elif 11 < people <= 18:
        discount += 0.25

elif season == "Autumn":
    price = 4200

    if people <= 6:
        discount += 0.1
    elif 7 <= people <= 11:
        discount += 0.15
    elif 11 < people <= 18:
        discount += 0.25

elif season == "Winter":
    price = 2600

    if people <= 6:
        discount += 0.1
    elif 7 <= people <= 11:
        discount += 0.15
    elif 11 < people <= 18:
        discount += 0.25

price = price * (1 - discount)

add_discount = 0
if season != "Autumn" and people % 2 == 0:
    add_discount += 0.05

add_price = price * (1 - add_discount)

if budget >= price:
    print("Yes! You have %.2f leva left." % (budget - add_price))
else:
    print("Not enough money! You need %.2f leva." % (add_price - budget))
