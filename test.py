from app.calculator.gpa import calculate_gpa
from app.model.course import Course

courses = [
    Course(name="Математика", credits=8, grade="A"),
    Course(name="Физика", credits=8, grade="B+"),
]

result = calculate_gpa(courses)
print(result)