n = int(input())

sum = 0

while n > 0:
    money = float(input())
    if money < 0:
        print("Invalid operation!")
        break
    else:
        sum += money
        n -= 1
        print("Increase: %.2f" % money)

print("Total: %.2f" % sum)
