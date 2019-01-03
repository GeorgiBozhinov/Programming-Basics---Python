table_num = int(input())
table_length = float(input())
table_width = float(input())

common_area = table_num * (table_length + 2 * 0.30) * (table_width + 2 * 0.30);
box_area = table_num * (table_length / 2) * (table_length / 2);

price_USD = common_area * 7 + box_area * 9;
price_LV = price_USD * 1.85;

print("%.2f" % price_USD + " " + "USD")
print("%.2f" % price_LV + " " + "BGN")
