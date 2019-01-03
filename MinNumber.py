numbers_of_input_digits = int(input())

number = int(input())
min_number = number

counter = 1

while True:
    if min_number > number:
        min_number = number

    if counter == numbers_of_input_digits:
        break

    number = int(input())
    counter += 1

print("%d" % min_number)
