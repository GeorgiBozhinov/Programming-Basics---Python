contestant_one = int(input())
contestant_two = int(input())
contestant_three = int(input())

sum_contestant_times = contestant_one + contestant_two + contestant_three
contestant_time_minutes = sum_contestant_times / 60

if sum_contestant_times < 10:
    print("0:0%.f" % sum_contestant_times)
elif sum_contestant_times > 0 and sum_contestant_times < 59:
    print("0:%.0f" % sum_contestant_times)
elif sum_contestant_times >= 60 and sum_contestant_times <= 119:
    calc_sec = sum_contestant_times - 60
    if calc_sec < 10:
        print("1:0%.0f" % calc_sec)
    else:
        print("1:%.0f" % calc_sec)
elif sum_contestant_times > 120 and sum_contestant_times < 179:
    sec = sum_contestant_times - 120
    if sec < 10:
        print("2:0%.0f" % sec)
    else:
        print("2:%.0f" % sec)
