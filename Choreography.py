import math

number_of_steps = int(input())
number_of_dancers = int(input())
number_of_days = int(input())

steps_per_days = ((number_of_steps / number_of_days) / number_of_steps) * 100
percent_steps_per_dancer = math.ceil(steps_per_days) / number_of_dancers

whole_dancer_steps = percent_steps_per_dancer*number_of_dancers
if whole_dancer_steps <= 13:
    print("Yes, they will succeed in that goal! %.2f" % percent_steps_per_dancer + "%.")
else:
    print("No, They will not succeed in that goal! Required %.2f" % percent_steps_per_dancer + "% steps to be learned per day.")
