numbers_of_input_digits = int(input())

number = int(input())
max_number = number

counter = 1

while True:
    if max_number < number:
        max_number = number

    if counter == numbers_of_input_digits:
        break

    number = int(input())
    counter += 1

print("%d" % max_number)
