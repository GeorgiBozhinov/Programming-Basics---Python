num = int(input())

bonus_points = 0
if num % 2 == 0:
    bonus_points += 1
elif num % 10 == 5:
    bonus_points += 2

if num <= 100:
    bonus_points += 5
elif num > 100 and num <= 1000:
    bonus_points += num * 0.20
else:
    bonus_points += num * 0.10

if bonus_points == int(bonus_points):
    print("%.f" % bonus_points)
    print("%.f" % (num + bonus_points))
else:
    print("%.1f" % bonus_points)
    print("%.1f" % (num + bonus_points))