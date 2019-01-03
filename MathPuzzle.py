number = int(input())

combinations = 0

for num1 in range(1, 31):
    for num2 in range(1, 31):
        for num3 in range(1, 31):
            if num1 < num2 < num3 and (num1 + num2 + num3) == number:
                print("%d + %d + %d = %d" % (num1, num2, num3, number))
                combinations += 1
            elif num1 > num2 > num3 and (num1 * num2 * num3) == number:
                print("%d * %d * %d = %d" % (num1, num2, num3, number))
                combinations += 1

if combinations == 0:
    print("No!")