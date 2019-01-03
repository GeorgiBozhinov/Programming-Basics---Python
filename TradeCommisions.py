town = input()
cells = float(input())

price = 0

if town == "Sofia":
    if cells >= 0 and cells <= 500:
        price += cells * 0.05
    elif cells > 500 and cells <= 1000:
        price += cells * 0.07
    elif cells > 1000 and cells <= 10000:
        price += cells * 0.08
    else:
        price += cells * 0.12

elif town == "Varna":
    if cells >= 0 and cells <= 500:
        price += cells * 0.045
    elif cells > 500 and cells <= 1000:
        price += cells * 0.075
    elif cells > 1000 and cells <= 10000:
        price += cells * 0.10
    else:
        price += cells * 0.13

elif town == "Plovdiv":
    if cells >= 0 and cells <= 500:
        price += cells * 0.055
    elif cells > 500 and cells <= 1000:
        price += cells * 0.08
    elif cells > 1000 and cells <= 10000:
        price += cells * 0.12
    elif cells > 10000:
        price += cells * 0.145

if price == 0:
    print("error")
else:
    print("%.2f" % price)
