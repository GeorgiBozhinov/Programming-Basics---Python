uiski_price = float(input())
beer_quantity = float(input())
wine_quantity = float(input())
rakia_quantity = float(input())
uiski_quantity = float(input())

rakia_price = uiski_price / 2;
wine_price = rakia_price - (rakia_price * 0.40);
beer_price = rakia_price - (rakia_price * 0.80);

rakia_sum = rakia_price * rakia_quantity;
wine_sum = wine_price * wine_quantity;
beer_sum = beer_price * beer_quantity;
uiski_sum = uiski_price * uiski_quantity;

end_sum = rakia_sum + wine_sum + beer_sum + uiski_sum;
print("%.2f" % end_sum)
