import math
type_of_year = input()
holidays = int(input())
weekends_at_home = int(input())

weekends_in_sofia = 48 - weekends_at_home
saturday_games_in_sofia = weekends_in_sofia * 3 / 4

holidays_games_in_sofia = holidays * 2 / 3
sum_of_games_in_sofia_and_home = saturday_games_in_sofia + weekends_at_home + holidays_games_in_sofia

additional_games = 0

if type_of_year == "leap":
    additional_games += sum_of_games_in_sofia_and_home * 0.15

all_games = additional_games + sum_of_games_in_sofia_and_home

print(math.floor(all_games))
