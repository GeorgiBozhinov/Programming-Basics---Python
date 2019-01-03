football_team = input()
souvenir = input()
number_of_souvenirs = int(input())

total = 0.0
country_bool = False

if not (football_team == 'Argentina' or football_team == 'Brazil'
        or football_team == 'Croatia' or football_team == 'Denmark'):
    print("Invalid country!")

elif not (souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'):
    print("Invalid stock!")

else:
    if football_team == 'Argentina':
        if souvenir == 'flags':
            total = number_of_souvenirs * 3.25
        elif souvenir == 'caps':
            total = number_of_souvenirs * 7.20
        elif souvenir == 'posters':
            total = number_of_souvenirs * 5.10
        else:
            total = number_of_souvenirs * 1.25

    elif football_team == 'Brazil':
        if souvenir == 'flags':
            total = number_of_souvenirs * 4.20
        elif souvenir == 'caps':
            total = number_of_souvenirs * 8.50
        elif souvenir == 'posters':
            total = number_of_souvenirs * 5.35
        else:
            total = number_of_souvenirs * 1.20

    elif football_team == 'Croatia':
        if souvenir == 'flags':
            total = number_of_souvenirs * 2.75
        elif souvenir == 'caps':
            total = number_of_souvenirs * 6.90
        elif souvenir == 'posters':
            total = number_of_souvenirs * 4.95
        else:
            total = number_of_souvenirs * 1.10

    else:
        if souvenir == 'flags':
            total = number_of_souvenirs * 3.10
        elif souvenir == 'caps':
            total = number_of_souvenirs * 6.50
        elif souvenir == 'posters':
            total = number_of_souvenirs * 4.80
        else:
            total = number_of_souvenirs * 0.90

    print("Pepi bought %d %s of %s for %.2f lv." %
          (number_of_souvenirs, souvenir, football_team, total))