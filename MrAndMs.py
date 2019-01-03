a = float(input())
str = input()

if a < 16 and str == "m":
    print("Master")
if a < 16 and str == "F":
    print("Miss")
if a < 16 and str == "f":
    print("Miss")

if a >= 16 and str == "m":
    print("Mr.")
if a >= 16 and str == "f":
    print("Ms.")
