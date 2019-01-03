num_one = int(input())
num_two = int(input())
symbol = input()

type_even_odd = ""

if symbol == "//" or symbol == "%" and num_two == 0:
    print("Cannot divide %d by zero" % num_one)
else:
    if symbol == "+":
        if (num_one + num_two) % 2 == 0:
            type_even_odd = "even"
        else:
            type_even_odd = "odd"
        print("%d %s %d = %d - %s" % (num_one, symbol, num_two, (num_one + num_two), type_even_odd))

    elif symbol == "-":
        if (num_one - num_two) % 2 == 0:
            type_even_odd = "even"
        else:
            type_even_odd = "odd"
        print("%d %s %d = %d - %s" % (num_one, symbol, num_two, (num_one - num_two), type_even_odd))

    elif symbol == "*":
        if (num_one * num_two) % 2 == 0:
            type_even_odd = "even"
        else:
            type_even_odd = "odd"
        print("%d %s %d = %d - %s" % (num_one, symbol, num_two, (num_one * num_two), type_even_odd))

    elif symbol == "/":
        print("%d %s %d = %.2f" % (num_one, symbol, num_two, (num_one / num_two)))

    else:
        print("%d %s %d = %d" % (num_one, symbol, num_two, (num_one % num_two)))
