number = int(input())
list = []
sum = 0
biggest_num = 0

for n in range(0,number):
    num = int(input())
    sum += num
    list  = list + [num]

    if num > biggest_num:
        biggest_num = num

end_sum = sum - biggest_num

if biggest_num == end_sum:
    print("Yes Sum = %d" % biggest_num)
else:
    for nums in list:
    print("No Diff = %d" % end_sum)

