a = float(input())

if a <= 10:
    print("slow")
elif a > 10 and a <= 50:
    print("average")
elif a > 50 and a <= 150:
    print("fast")
elif a > 150 and a <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
