num = int(input())

while not (1 <= num <= 100):
    print("Invalid number!")
    num = int(input())

print("The number is %d" % num)
