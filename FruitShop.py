fruit = input()
day_of_week = input()
quantity = float(input())

working_days = {'banana': 2.50, 'apple': 1.20, 'orange': 0.85, 'grapefruit': 1.45, 'kiwi': 2.70, 'pineapple': 5.50,
                'grapes': 3.85}
weekend_days = {'banana': 2.70, 'apple': 1.25, 'orange': 0.90, 'grapefruit': 1.60, 'kiwi': 3.00, 'pineapple': 5.60,
                'grapes': 4.20}

price = 0

if day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes":
        for key, value in weekend_days.items():
            if key == fruit:
                price += quantity * value
                print("%.2f" % price)
elif day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes":
        for key, value in working_days.items():
            if key == fruit:
                price += quantity * value
                print("%.2f" % price)

if price == 0:
    print('error')
