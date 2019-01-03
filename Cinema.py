type = input()
rows = int(input())
columns = int(input())

rows_by_columns = rows * columns
sum = 0

if type == "Premiere":
    sum += rows_by_columns * 12
elif type == "Normal":
    sum += rows_by_columns * 7.5
else:
    sum += rows_by_columns * 5

print("%.2f leva" % sum)
