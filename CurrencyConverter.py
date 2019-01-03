input_num = float(input())
str_input_curr = input()
str_output_curr = input()

if str_input_curr == "USD" and str_output_curr == "BGN":
    sum_BGN = input_num * 1.79549
    print("%.2f" % sum_BGN + " " + "BGN")

if str_input_curr == "USD" and str_output_curr == "EUR":
    calc_BGN = input_num * 1.79549
    sum_EUR = calc_BGN / 1.95583
    print("%.2f" % sum_EUR + " " + "EUR")

if str_input_curr == "BGN" and str_output_curr == "EUR":
    # calc_GBP = input_num * 1.79549
    sum_BGN_EUR = input_num/1.95583
    print("%.2f" % sum_BGN_EUR + " " + "EUR")

if str_input_curr == "EUR" and str_output_curr == "GBP":
    calc_EUR_GBP = input_num * 1.95583
    sum_EUR_GBP = calc_EUR_GBP / 2.53405
    print("%.2f" % sum_EUR_GBP)

if str_input_curr == "GBP" and str_output_curr == "USD":
    calc_GBP_USD = input_num * 2.53405
    sum_GBP_USD = calc_GBP_USD / 1.79549
    print("%.2f" % sum_GBP_USD)


