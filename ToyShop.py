trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
number_of_toys = puzzles + dolls + bears + minions + trucks

if number_of_toys >= 50:
    discount = price * 0.25
    price -= discount

rent = price * 0.10
end_sum = price - rent

if end_sum >= trip_price:
    end_sum -= trip_price
    print("Yes! %.2f lv left." % end_sum)
else:
    end_sum -= trip_price
    print("Not enough money! %.2f lv needed." % abs(end_sum))