import math

str = input()

if str == "square":
    side = float(input())
    square_area = side * side
    print("%.3f" % square_area)
elif str == "rectangle":
    a = float(input())
    b = float(input())
    rect_area = a * b
    print("%.3f" % rect_area)
elif str == "circle":
    c = float(input())
    circle_area = math.pi * c * c
    print("%.3f" % circle_area)
else:
    d = float(input())
    e = float(input())
    triangle_area = d * e / 2
    print("%.3f" % triangle_area)
