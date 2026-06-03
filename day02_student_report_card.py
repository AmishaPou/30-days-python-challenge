# Day 2 - Student Report Card Generator

# Read student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

english = float(input("Enter English marks: "))
math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))

# Store details in a dictionary
student_info = {
    "name": student_name,
    "roll_number": roll_number,
    "marks": [english, math, science]
}

# Calculate total and percentage
total_marks = english + math + science
percentage = (total_marks / 300) * 100

# Pass/Fail using logical operators
passed = (
    english >= 40 and
    math >= 40 and
    science >= 40
)

# Grade assignment using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Nested if with set membership test
if passed:
    if grade in {"A+", "A"}:
        remark = "Distinction"
    else:
        remark = "Pass"
else:
    remark = "Fail"

# Ternary expression
status = "PASS" if passed else "FAIL"

# Print Report Card

print("        STUDENT REPORT CARD")
print("=" * 40)

print(f"Name       : {student_info['name']}")
print(f"Roll No    : {student_info['roll_number']}")
print(f"English    : {english}")
print(f"Math       : {math}")
print(f"Science    : {science}")

print("-" * 40)

print(f"Total      : {total_marks}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Remark     : {remark}")
print(f"Status     : {status}")

