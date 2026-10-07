num_courses = int(input("Number of courses: "))

total_points = 0
total_credits = 0

for i in range(num_courses):
    course_name = input("Course name: ")
    credit_hours = float(input("Credit hours: "))
    grade_point = float(input("Grade point: "))

    total_points += credit_hours * grade_point
    total_credits += credit_hours

gpa = total_points / total_credits

print(f"Semester GPA: {gpa:.2f}")