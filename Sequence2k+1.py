num = int(input())

n = 1

while n <= num:
    calc = (n - 1) * 2 + 1
    if (calc == 1 or calc == 3 or calc == 7 or
        calc == 15 or calc == 31 and calc <= num):
        print(calc)

    n += 1
