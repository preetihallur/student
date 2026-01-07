def show_grade_criteria():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------\n")

def show_student_details(name, department, semester):
    print("\n--- Student Details ---")
    print(f"Name: {name}")
    print(f"Department: {department}")
    print(f"Semester: {semester}\n")

def show_subject_marks(marks):
    print("--- Subject Marks ---")
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark}")
    print()

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

def main():
    show_grade_criteria()

    # User input for student details
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    # User input for subject marks
    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)

    show_student_details(name, department, semester)
    show_subject_marks(marks)

    avg = calculate_average(marks)
    grade = calculate_grade(avg)

    print(f"Average Marks: {avg:.2f}")
    print(f"Final Grade: {grade}")

if __name__ == "__main__":
    main()
