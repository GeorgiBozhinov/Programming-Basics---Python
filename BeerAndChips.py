import math
name = input()
budjet = float(input())
number_of_bottles = int(input())
number_of_packets_with_chips = int(input())

beer_price = 1.20 * number_of_bottles
price_per_chips = beer_price * 0.45
price_for_all_chips = math.ceil(price_per_chips * number_of_packets_with_chips)

end_sum = beer_price + price_for_all_chips

if end_sum <= budjet:
    print("%s bought a snack and has %.2f leva left." % (name, budjet - end_sum))
else:
    print("%s needs %.2f more leva!" % (name, end_sum - budjet))
