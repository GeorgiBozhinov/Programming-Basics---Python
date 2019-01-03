num = input()

steps = 0

while True:
    if input == "Going home" or steps >= 10000:
        break;

    steps += int(num)
    num = input()

print("Goal reached! Good job!")
