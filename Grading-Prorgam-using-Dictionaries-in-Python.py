student_scores = {
    "Jawad": 81,
    "Adan": 67,
    "Danial": 45,
    "Haris": 86,
    "Hammad": 64
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
