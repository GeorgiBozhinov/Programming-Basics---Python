money = float(input())
number_of_coins = 0

while money > 0:
    if money - 2 >= 0:
        number_of_coins += 1
        money = money - 2
    else:
        break
while money > 0:
        number_of_coins += 1
        money = money - 1
    else:
        break
while money > 0:
    if money - 0.5 >= 0:
        number_of_coins += 1
        money = money - 0.5
    else:
        break
while money > 0:
    if money - 0.2 >= 0:
        number_of_coins += 1
        money = money - 0.2
    if money - 1 >= 0:
    else:
        break
while money > 0:
    if money - 0.1 >= 0:
        number_of_coins += 1
        money = money - 0.1
    else:
        break
while money > 0:
    if money - 0.05 >= 0:
        number_of_coins += 1
        money = money - 0.05
    else:
        break
while money > 0:
    if money - 0.02 >= 0:
        number_of_coins += 1
        money = money - 0.02
    else:
        break
while money > 0:
    if money - 0.01 >= 0:
        number_of_coins += 1
        money = money - 0.01
    else:
        break
print(number_of_coins)
