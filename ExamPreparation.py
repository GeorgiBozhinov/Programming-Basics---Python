num_of_bad_grades = int(input())

task_name = input()
number_of_problems = 0
grades_sum = 0
last_problem = ""

poor_grades = 0

while True:
    if task_name == "Enough":
        print("Average score: %.2f" % (grades_sum / number_of_problems))
        print("Number of problems: %d" % number_of_problems)
        print("Last problem: %s" % last_problem)
        break

    grade = int(input())
    grades_sum += grade
    number_of_problems += 1

    if grade <= 4:
        poor_grades += 1
        if poor_grades == num_of_bad_grades:
            print("You need a break, %d poor grades." % poor_grades)
            break

    task_name = input()

    if task_name != "Enough":
        last_problem = task_name


