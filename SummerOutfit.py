graduses = int(input())
day = input()

clothes = ""
shoes = ""

if graduses >= 10 and graduses <= 18:
    if day == "Morning":
        clothes = "Sweatshirt"
        shoes = "Sneakers"
    elif day == "Afternoon":
        clothes = "Shirt"
        shoes = "Moccasins"
    else:
        clothes = "Shirt"
        shoes = "Moccasins"
elif graduses > 18 and graduses <= 24:
    if day == "Morning":
        clothes = "Shirt"
        shoes = "Moccasins"
    elif day == "Afternoon":
        clothes = "T-Shirt"
        shoes = "Sandals"
    else:
        clothes = "Shirt"
        shoes = "Moccasins"
elif graduses >= 25:
    if day == "Morning":
        clothes = "T-Shirt"
        shoes = "Sandals"
    elif day == "Afternoon":
        clothes = "Swim Suit"
        shoes = "Barefoot"
    else:
        clothes = "Shirt"
        shoes = "Moccasins"

print("It's %d degrees, get your %s and %s." % (graduses, clothes, shoes))
