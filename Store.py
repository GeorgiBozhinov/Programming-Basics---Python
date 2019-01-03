str_product = input().lower()
str_city = input().lower()
quantity = float(input())

coffee = 0
water = 0
beer = 0
sweets = 0
peanuts = 0

if str_city == "sofia":
    if str_product == "coffee":
        coffee = quantity * 0.50
        print("%.2f" % coffee)
    elif str_product == "water":
        water = quantity * 0.80
        print("%.2f" % water)
    elif str_product == "beer":
        beer = quantity * 1.20
        print("%.2f" % beer)
    elif str_product == "sweets":
        sweets = quantity * 1.45
        print("%.2f" % sweets)
    elif str_product == "peanuts":
        peanuts = quantity * 1.60
        print("%.2f" % peanuts)

elif str_city == "plovdiv":
    if str_product == "coffee":
        coffee = quantity * 0.40
        print("%.2f" % coffee)
    elif str_product == "water":
        water = quantity * 0.70
        print("%.2f" % water)
    elif str_product == "beer":
        beer = quantity * 1.15
        print("%.2f" % beer)
    elif str_product == "sweets":
        sweets = quantity * 1.30
        print("%.2f" % sweets)
    elif str_product == "peanuts":
        peanuts = quantity * 1.50
        print("%.2f" % peanuts)

elif str_city == "varna":
    if str_product == "coffee":
        coffee = quantity * 0.45
        print("%.2f" % coffee)
    elif str_product == "water":
        water = quantity * 0.70
        print("%.2f" % water)
    elif str_product == "beer":
        beer = quantity * 1.10
        print("%.2f" % beer)
    elif str_product == "sweets":
        sweets = quantity * 1.35
        print("%.2f" % sweets)
    elif str_product == "peanuts":
        peanuts = quantity * 1.55
        print("%.2f" % peanuts)



