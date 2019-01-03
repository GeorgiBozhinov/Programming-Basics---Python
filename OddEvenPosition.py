num = int(input())

odd_sum = 0
odd_min = 0
odd_max = 0

even_sum = 0
even_min = 0
even_max = 0

for n in range(0, num):
    number = int(input())
    if number % 2 != 0:
        odd_sum += number
        if odd_min == 0:
            odd_min = number
        else:
            if number < odd_min:
                odd_min = number

        if number > odd_max:
            odd_max = number
    else:
        even_sum += number
        if number < even_min:
            if even_min == 0:
                even_min = number
            else:
                even_min = number
        if number > even_max:
            even_max = number

print("OddSum=%d," % odd_sum)
print("OddMin=%d," % odd_min)
print("OddMax=%d," % odd_max)
print("EvenSum=%d," % even_sum)
print("EvenMin=%d," % even_min)
print("EvenMax=%d," % even_max)
