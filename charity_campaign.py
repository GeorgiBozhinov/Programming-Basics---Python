days = int(input())
confectioner_num = int(input())
cake_num = int(input())
waffles_num = int(input())
pankakes_num = int(input())

cake_price_day = cake_num * 45;
waffles_price_day = waffles_num * 5.80;
pankakes_price_day = pankakes_num * 3.20;

whole_sum_day = (cake_price_day + waffles_price_day + pankakes_price_day) * confectioner_num;
whole_sum_from_campaign = whole_sum_day * days;

end_sum = whole_sum_from_campaign - (whole_sum_from_campaign * 0.125);
print("%.2f" % end_sum)
