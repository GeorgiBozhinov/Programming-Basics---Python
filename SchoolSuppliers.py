pens = int(input())
markers = int(input())
liter_preparation = float(input())
discount = int(input())

books_price_math = pens * 5.80
books_price_bulgarian_language = markers * 7.20
preparation_price = liter_preparation * 1.20

price_of_all = books_price_math + books_price_bulgarian_language + preparation_price

price_after_discount = price_of_all - ((price_of_all * discount) / 100)

print("%.3f" % price_after_discount)
