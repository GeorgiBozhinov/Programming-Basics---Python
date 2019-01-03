import  math
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

distance_by_time = distance_in_meters * time_in_seconds
additional_seconds = math.floor((distance_in_meters / 50)) * 30
distance_by_time += additional_seconds

if record_in_seconds <= distance_by_time:
    print("No! He was %.2f seconds slower." % (distance_by_time-record_in_seconds))
else:
    print("Yes! The new record is %.2f seconds." % distance_by_time)
