width = int(input())
length = int(input())

cake_size = width * length
sum = 0

while True:
    pieces = input()

    if pieces == "STOP":
        if cake_size > sum:
            calc = cake_size - sum
            print("%d pieces are left." % calc)
        break

    sum += int(pieces)

    if sum > cake_size:
        calc_two = sum - cake_size
        print("No more cake left! You need %d pieces more." % calc_two)
        break


