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
            semester = sys.argv[3]
            marks = [
                float(sys.argv[4]),
                float(sys.argv[5]),
                float(sys.argv[6])
            ]

        # Case 2: Interactive console input
        else:
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")
            semester = input("Enter Semester: ")

            marks = []
            for i in range(3):
                mark = float(input(f"Enter marks for Subject {i+1}: "))
                marks.append(mark)

        avg = calculate_average(marks)
        grade = calculate_grade(avg)

        print("\n=== Student Details ===")
        print("Name       :", name)
        print("Department :", department)
        print("Semester   :", semester)

        print("\n=== Subject Marks ===")
        for i, mark in enumerate(marks, start=1):
            print(f"Subject {i}: {mark}")

        print("\nAverage Marks :", f"{avg:.2f}")
        print("Final Grade   :", grade)

    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")
