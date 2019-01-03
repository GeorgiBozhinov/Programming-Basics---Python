needed_money_for_vacation = float(input())
available_money = float(input())

num_of_days = 0
times_spend = 0

while True:
    type = input()
    money = float(input())

    if type == "save":
        available_money += money
    else:
        times_spend += 1
        if available_money < money:
            available_money = 0
        else:
            available_money -= money

    num_of_days += 1

    if needed_money_for_vacation == available_money:
        print("You saved the money for %d days." % num_of_days)
        break

    if times_spend == 5:
        print("You can't save the money.")
        break

    continue
