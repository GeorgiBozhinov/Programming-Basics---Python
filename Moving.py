width = int(input())
length = int(input())
height = int(input())

cubic_meters = width * length * height
boxes = input()

boxes_sum = 0

while True:
    if boxes == "Done":
        left_cubic_meters = cubic_meters - boxes_sum
        print("%d Cubic meters left." % left_cubic_meters)
        break

    boxes_sum += int(boxes)

    if cubic_meters < boxes_sum:
        needed_more_space = boxes_sum - cubic_meters
        print("No more free space! You need %d Cubic meters more." % needed_more_space)
        break


    boxes = input()

