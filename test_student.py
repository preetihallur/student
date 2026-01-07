# student.py
# Student Grade Calculator

def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    print("Run this program directly to calculate grades")
