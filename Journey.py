budget = float(input())
season = input()

percents = 0

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        percents += 0.30
        print("Camp - %.2f" % (budget * percents))
    else:
        percents += 0.70
        print("Hotel - %.2f" % (budget * percents))
elif budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        percents += 0.40
        print("Camp - %.2f" % (budget * percents))
    else:
        percents += 0.80
        print("Hotel - %.2f" % (budget * percents))
elif budget > 1000:
    percents += 0.90
    print("Somewhere in Europe")
    print("Hotel - %.2f" % (budget * percents))

