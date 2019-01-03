num_of_digits = int(input())

sum = 0

for numbers in range(1, num_of_digits + 1):
    input_numbers = float(input())
    sum += input_numbers

print(sum)
