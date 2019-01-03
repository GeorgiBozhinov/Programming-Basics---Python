dict = {'mm': 1000, 'cm': 100, 'mi': 0.000621371192, 'in': 39.3700787, 'km': 0.001, 'ft': 3.2808399,
        'yd': 1.0936133, 'm':1}

num = float(input())
metric_one = input()
metric_two = input()

sum = 0
if metric_one == metric_two:
    print(num)
else:
    for key, value in dict.items():
        if key == metric_one:
            sum += num / value

    for key, value in dict.items():
        if key == metric_two:
            sum = sum * value

            print("%.8f" % sum)
