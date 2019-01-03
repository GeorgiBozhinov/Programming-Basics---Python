import math

first_brother_time = float(input())
second_brother_time = float(input())
third_brother_time = float(input())
father_time_for_fishing = float(input())

common_time = 1 / (1 / first_brother_time + 1 / second_brother_time + 1 / third_brother_time)
time_plus_rest = common_time + (common_time * 0.15)

print("Cleaning time: %.2f" % time_plus_rest)

time_left = father_time_for_fishing - time_plus_rest
if time_left > 0:
    print("Yes, there is a surprise - time left -> %.0f hours." % math.floor(time_left))
else:
    print("No, there isn't a surprise - shortage of time -> %.0f hours." % math.ceil(
        time_plus_rest - father_time_for_fishing))
