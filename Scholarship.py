import math

income = float(input())
average_progress = float(input())
average_salary = float(input())

scholarship_social = 0
scholarship_excellent = 0

if income > average_salary:
    if average_progress < 5.50:
        scholarship_excellent = 0
elif income <= average_salary:
    if average_progress > 4.50:
        scholarship_social += average_salary * 0.35
    if average_progress >= 5.50:
        scholarship_excellent += average_progress * 25

if scholarship_social <= 0 and scholarship_excellent <= 0:
    print("You cannot get a scholarship!")
elif scholarship_social > scholarship_excellent:
    print("You get a Social scholarship %.0f BGN" %
          math.floor(scholarship_social))
else:
        print("You get a scholarship for excellent results "
              "%.0f BGN" % math.floor(scholarship_excellent))
