number_of_sectors = int(input())
capacity = int(input())
ticket_price = float(input())

total_capacity = capacity * ticket_price
income_per_sector = total_capacity / number_of_sectors
money_for_charity = (total_capacity - (income_per_sector * 0.75))/8

print("Total income - %.2f BGN" % total_capacity)
print("Money for charity - %.2f BGN" % money_for_charity)