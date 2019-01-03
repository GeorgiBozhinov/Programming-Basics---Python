number_of_groups = int(input())

group = int(input())
counter = 1

group_Musala = 0
group_Monblan = 0
group_Kilimandjaro = 0
group_K2 = 0
group_Everest = 0

sum_of_all_people = 0

while True:
    sum_of_all_people += group

    if group <= 5:
        group_Musala += group
    elif 6 <= group <= 12:
        group_Monblan += group
    elif 13 <= group <= 25:
        group_Kilimandjaro += group
    elif 26 <= group <= 40:
        group_K2 += group
    else:
        group_Everest += group

    if counter == number_of_groups:
        break

    group = int(input())
    counter += 1

group_Musala = (group_Musala / sum_of_all_people) * 100
group_Monblan = (group_Monblan / sum_of_all_people) * 100
group_Kilimandjaro = (group_Kilimandjaro / sum_of_all_people) * 100
group_K2 = (group_K2 / sum_of_all_people) * 100
group_Everest = (group_Everest / sum_of_all_people) * 100

print("{0:0.2f}%".format(group_Musala))
print("{0:0.2f}%".format(group_Monblan))
print("{0:0.2f}%".format(group_Kilimandjaro))
print("{0:0.2f}%".format(group_K2))
print("{0:0.2f}%".format(group_Everest))

