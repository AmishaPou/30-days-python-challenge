# Day 2 - Student Report Card Generator

student_name = input("Enter student name:")
student_id = input("Enter roll number:")

english = float(input("Enter English marks:"))
math = float(input("Enter Math marks:"))
science = float(input("Enter Science marks:"))

student_info = {
    "name": student_name,
    "id": student_id,
    "scores":[english, math,science]
}

total_marks = english+math+science
average_marks = total_marks/3

passed ={
    english>=40 and
    math>=40 and
    science>=40
}
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B+"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
else:
    grade = "F"

if passed:
    if grade in ["A+", "A"]:
        division = "Distinction"
    elif grade == "B+":
        division = "First Division"
    else:
        division = "Second Division"
else:
    division = "Fail"

status = "PASS" if passed else "FAIL"


print(f"{'STUDENT REPORT CARD' :}")
print("-" * 30)
print("Name        :", student_info["name"])
print("Roll No     :", student_info["id"])
print("Marks       :", student_info["scores"])
print("Total       :", total_marks)
print("Average     :", round(average_marks, 2))
print("Grade       :", grade)
print("Division    :", division)
print("Final Status:", status)