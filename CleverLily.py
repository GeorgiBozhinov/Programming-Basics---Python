lily_age = int(input())
washing_machine_price = float(input())
single_price = int(input())

sum = 0
dolls = 0
numbers_of_years_lily_taken_money = 0

list = []

temp = 0

for n in range(1, lily_age + 1):
    if n % 2 == 0:
        temp = temp + 10
        list = list + [temp]
        numbers_of_years_lily_taken_money += 1
    else:
        dolls += 1

for m in list:
    sum += m

sum += (dolls * single_price) - numbers_of_years_lily_taken_money
# money_taken_from_brother = sum - numbers_of_years_lily_taken_money

if sum >= washing_machine_price:
    print("Yes! %.2f" % (sum - washing_machine_price))
else:
    calc = washing_machine_price - sum
    print("No! %.2f" % abs(calc))
