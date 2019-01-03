flower = input()
number_of_flowers = int(input())
budget = int(input())

end_price = 0

if flower == "Roses":
    end_price += number_of_flowers * 5
    if number_of_flowers > 80:
        end_price -= end_price * 0.10
elif flower == "Dahlias":
    end_price += number_of_flowers * 3.80
    if number_of_flowers > 90:
        end_price -= end_price * 0.15
elif flower == "Tulips":
    end_price += (number_of_flowers * 2.80)
    if number_of_flowers > 80:
        end_price -= end_price * 0.15
elif flower == "Narcissus":
    end_price += number_of_flowers * 3
    if number_of_flowers < 120:
        end_price += end_price * 0.15
elif flower == "Gladiolus":
    end_price += number_of_flowers * 2.50
    if number_of_flowers < 80:
        end_price += end_price * 0.20

if end_price > budget:
    print("Not enough money, you need %.2f leva more." % (end_price - budget))
else:
    print("Hey, you have a great garden with %d %s and %.2f leva left." % (
        number_of_flowers, flower, (budget - end_price)))
