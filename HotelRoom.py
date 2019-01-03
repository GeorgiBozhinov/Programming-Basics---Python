month = input()
nights = int(input())

night_studio = 0
night_apartment = 0

discount_studio = 0
discount_apartment = 0

if month == "May" or month == "October":
    night_studio += 50
    night_apartment += 65

    if nights > 14:
        night_studio -= night_studio * 0.30
    elif nights > 7:
        night_studio -= night_studio * 0.05


elif month == "June" or month == "September":
    night_studio += 75.20
    night_apartment += 68.70
    if nights > 14:
        night_studio -= night_studio * 0.20
else:
    night_studio += 76
    night_apartment += 77

if nights > 14:
    night_apartment -= night_apartment * 0.10

studio_nights = night_studio * nights
apartment_nights = night_apartment * nights


print("Apartment: %.2f lv." % apartment_nights)
print("Studio: %.2f lv." % studio_nights)
