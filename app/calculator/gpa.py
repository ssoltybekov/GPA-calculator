from app.model.course import Course

def grade_to_points(grade: str) -> float:
    grades = {
        "A": 4.00,
        "A-": 3.67,
        "B+": 3.33,
        "B": 3.00,
        "B-": 2.67,
        "C+": 2.33,
        "C": 2.00,
        "C-": 1.67,
        "D+": 1.33,
        "D": 1.00,
        "F": 0.00
    }
    return grades[grade]

def calculate_gpa(courses: list[Course]) -> float:
    total_points = 0
    total_credits = 0

    for course in courses:
        points = grade_to_points(course.grade)
        total_points += points * course.credits
        total_credits += course.credits

    return total_points/total_credits

