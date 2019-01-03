budjet = int(input())
number_of_objects = int(input())

total_sum = 0.0

for prod in range(0, number_of_objects):
    object = input()

    if object == 'hoodie':
        total_sum += 30
    elif object == 'keychain':
        total_sum += 4
    elif object == 'T-shirt':
        total_sum += 20
    elif object == 'flag':
        total_sum += 15
    else:
        total_sum += 1

if budjet >= total_sum:
    print("You bought %d items and left with %d lv." %
          (number_of_objects, (budjet - total_sum)))
else:
    print("Not enough money, you need %d more lv." % (total_sum - budjet))
