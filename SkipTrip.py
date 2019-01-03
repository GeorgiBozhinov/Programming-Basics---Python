days = int(input())
type_of_apartment = input()
grade = input()

nights = days - 1
price = 0.0



if type_of_apartment == "apartment":
    price += nights * 25
    if nights < 10:
        price = price - (price * 0.30)
    elif 10 < nights < 15:
        price = price - (price * 0.35)
    else:
        price = price - (price * 0.50)
elif type_of_apartment == "president apartment":
    price += nights * 35
    if nights < 10:
        price = price - (price * 0.10)
    elif 10 < nights < 15:
        price = price - (price * 0.15)
    else:
        price = price - (price * 0.20)
else:
    price += nights * 18

if grade == "positive":
    price = price + (price * 0.25)
else:
    price = price - (price * 0.10)

print("%.2f" % price)
