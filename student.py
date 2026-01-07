# grade_calculator.py
# Program to calculate student grade

import sys

def show_grade_criteria():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------\n")

def calculate_average(marks):
    return sum(marks) / len(marks)

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
    print("=== Student Grade Calculator ===")
    show_grade_criteria()

    try:
        # Case 1: CLI / Jenkins arguments
        # python grade_calculator.py Name Dept Sem m1 m2 m3
        if len(sys.argv) == 7:
            name = sys.argv[1]
            department = sys.argv[2]
            semester = sys.ar
