hours = int(input())
minutes = int(input())

if (minutes + 15) > 59:
    hours += 1
    minutes += 15
    minutes -= 60
    if hours > 23:
        hours = 0
else:
    minutes += 15

if minutes < 10:
    print("%d:0%d" % (hours, minutes))
else:
    print("%d:%d" % (hours, minutes))
