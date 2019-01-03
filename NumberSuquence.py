nums = input()

max_num = int(nums)
min_num = int(nums)

while nums != "END":
    if int(nums) > max_num:
        max_num = int(nums)
    elif int(nums) < min_num:
        min_num = int(nums)
    nums = input()

print("Max number: %d" % max_num)
print("Min number: %d" % min_num)
