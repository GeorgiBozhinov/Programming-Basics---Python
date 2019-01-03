import  math
numbers_input = int(input())

rotation = numbers_input * 2
num = int(input())

left_sum = 0
right_sum = 0

for n in range(0,rotation):
    if n+1 > numbers_input:
        right_sum += num
    else:
        left_sum += num

    if n+1 == rotation:
        break

    num = int(input())

if left_sum == right_sum:
    print("Yes, sum = %d" % left_sum)
else:
    calc_diff = left_sum - right_sum
    print("No, diff = %d" % abs(calc_diff))
