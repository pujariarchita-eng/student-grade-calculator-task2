def calculate_grade(marks):
    """Return the grade for marks between 0 and 100."""
    if not isinstance(marks, (int, float)):
        return "Invalid marks"

    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


# Manually created student marks for testing
students = {
    "Aarav": 95,
    "Diya": 86,
    "Rohan": 74,
    "Sneha": 63,
    "Kabir": 48,
    "Invalid_Low": -5,
    "Invalid_High": 105
}

print("Student Grade Calculator")
print("-" * 30)

for name, marks in students.items():
    print(f"{name}: {marks} marks -> Grade {calculate_grade(marks)}")
