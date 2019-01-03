import  math
record_sec = float(input())
distance_meters = float(input())
time_in_sec_for_one_meter = float(input())

distance_to_go_through = distance_meters *\
                         time_in_sec_for_one_meter
additional_sec_per_15_meters = math.floor(distance_meters / 15) \
                               * 12.5
distance_to_go_through += additional_sec_per_15_meters

if record_sec <= distance_to_go_through:
    print("No, he failed! He was %.2f seconds "
          "slower." % (distance_to_go_through - record_sec))
else:
    print("Yes, he succeeded! The new world"
          " record is %.2f seconds." % distance_to_go_through)