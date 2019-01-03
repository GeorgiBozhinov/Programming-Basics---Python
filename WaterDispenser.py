water = int(input())

water_input = 0
times_tapped = 0

while water_input < water:
    command = input()
    times_tapped += 1

    if command == "Easy":
        water_input += 50
    elif command == "Medium":
        water_input += 100
    else:
        water_input += 200

if water_input == water:
    print("The dispenser has been tapped %d times." % times_tapped)
else:
    difference = water_input - water
    print("%dml has been spilled." % difference)
