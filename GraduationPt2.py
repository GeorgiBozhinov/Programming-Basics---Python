name = input()

sum = 0.0
counter = 0
negativeGrades = 0.0

while counter <= 12:
    grade = float(input())
    if grade >= 4.00:
        sum += grade
        counter += 1
    else:
        negativeGrades += 1
        counter += 1

    if negativeGrades >= 2:
        break

    # grade = float(input())


if negativeGrades > 0:
    print("{0} has been excluded at {1} grade".format(name, counter - 1))
else:
    print("{0} graduated. Average grade: {1:.2f}".format(name, (sum / 12)))
