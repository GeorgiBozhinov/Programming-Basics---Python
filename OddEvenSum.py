import math

numbers_input = int(input())

even_sum = 0
odd_sum = 0

if numbers_input > 0:
    num = int(input())

for n in range(0, numbers_input):
    if n % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

    if n + 1 == numbers_input:
        break

    num = int(input())

if even_sum == odd_sum:
    print("Yes Sum = %d" % even_sum)
else:
    if even_sum != 0:
        calc_diff = even_sum - odd_sum
        print("No Diff = %d" % abs(calc_diff))
