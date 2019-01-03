import math

football_team = input()
games = int(input())

points = 0
goal_difference = 0

goals_scored = 0
received_goals = 0

for matches in range(0, games):
    goals_in = int(input())
    goals_out = int(input())

    goals_scored += goals_in
    received_goals += goals_out

    goal_difference += goals_in - goals_out

    if goals_in > goals_out:
        points += 3
    elif goals_in == goals_out:
        points += 1

if goals_scored >= received_goals:
    print("%s has finished the group phase with %d points." % (football_team, points))
    print("Goal difference: %d." % goal_difference)
else:
    print("%s has been eliminated from the group phase." % football_team)
    print("Goal difference: %d." % goal_difference)
