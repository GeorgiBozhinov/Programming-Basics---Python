name = input()

sum = 0.0
counter = 1.0

while counter <= 12:
    grade = float(input())
    sum += grade
    counter += 1

print("{0} graduated. Average grade: {1:.2f}".format(name, sum/12))
