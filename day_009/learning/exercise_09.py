student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def convert_to_grade(score):
    if score > 90: 
        return "Outstanding"
    elif score > 80 and score < 91: 
        return "Exceeds Expectations"
    elif score > 70 and score < 81: 
        return"Acceptable"
    else:
        return "Fail"

student_grades = {}
for key, value in student_scores.items():
    student_grades[key] = convert_to_grade(value)
print(student_grades)
