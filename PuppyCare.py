food_for_puppy = int(input())

food_in_gr = input()
food_for_puppy = food_for_puppy * 1000

food_puppy_eat = 0

while True:
    if food_in_gr == "Adopted":
        break

    food_puppy_eat += int(food_in_gr)
    food_in_gr = input()

if food_puppy_eat <= food_for_puppy:
    print("Food is enough! Leftovers: "
          "%d grams." % (food_for_puppy - food_puppy_eat))
else:
    print("Food is not enough. "
          "You need %d grams more." % (food_puppy_eat - food_for_puppy) )
