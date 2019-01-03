word = input()

sum = 0

for w in word:
    if w == 'a':
        sum += 1
    elif w == 'e':
        sum += 2
    elif w == 'i':
        sum += 3
    elif w == 'o':
        sum += 4
    elif w == 'u':
        sum += 5

print(sum)
