number = int(input())

counter = 0
ticket_combination = ''
price = 0

for symbol1 in range(ord('B'), ord('L') + 1):
    for symbol2 in range(ord('f'), ord('a') + 1):
        for symbol3 in range(ord('A'), ord('C')):
            for symbol4 in range(1, 11):
                for symbol5 in range(10, 1, -1):
                    if chr(symbol1).isupper():
                        counter += 1
                    if counter == number:
                        ticket_combination += symbol1
                        ticket_combination += symbol2
                        ticket_combination += symbol3
                        ticket_combination += symbol4
                        ticket_combination += symbol5

                        price = symbol1 + symbol2
                        + symbol3 + symbol4 + symbol5
                        break

print("Ticket combination: %s" % ticket_combination)
print("Prize: %d lv." % price)
