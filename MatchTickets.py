budget = float(input())
category = input()
people = int(input())

money_for_transport = 0

if people >= 1 and people <= 4:
    money_for_transport += budget * 0.75
elif people >= 5 and people <= 9:
    money_for_transport += budget * 0.60
elif people >= 10 and people <= 24:
    money_for_transport += budget * 0.50
elif people >= 25 and people <= 49:
    money_for_transport += budget * 0.40
else:
    money_for_transport += budget * 0.25

money_left = budget - money_for_transport

ticket_price = 0

if category == "Normal":
    ticket_price += 249.99
else:
    ticket_price += 499.99

price_for_all_tickets = ticket_price * people

if price_for_all_tickets < money_left:
    sum = money_left - price_for_all_tickets
    print("Yes! You have %.2f leva left." % sum)
else:
    needed_sum = price_for_all_tickets - money_left
    print("Not enough money! You need %.2f leva." % needed_sum)
