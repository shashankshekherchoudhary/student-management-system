students = {}

def calculate_total(marks):
    total_sum = 0
    for mark in marks:
        total_sum += mark
    return total_sum


def calculate_percentage(total_marks, marks):
    return total_marks / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "Fail"


def add_student():
    while True:
        roll_number = input("Enter student roll number: ")
        if roll_number == "":
            print("Roll number cannot be empty!")
            continue
        if roll_number in students:
            print("Roll number already exists!")
            continue
        break

    while True:
        student_name = input("Enter student name: ").strip()
        if student_name == "":
            print("Student name should not be empty!")
            continue
        break

    subjects = ['Physics', 'Chemistry', 'Mathematics']
    marks = []

    for sub in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {sub} out of 100: "))
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Enter a number only.")

    total_marks = calculate_total(marks)
    student_percentage = calculate_percentage(total_marks, marks)
    student_grade = calculate_grade(student_percentage)

    student = {
        'student_name': student_name,
        'marks': marks,
        'total_marks': total_marks,
        'percentage': student_percentage,
        'grade': student_grade
    }

    students[roll_number] = student


def view_all_students():
    if not students:
        print("No student records found!")
        return

    for roll, details in students.items():
        print("Roll number:", roll)
        print("Student name:", details['student_name'])
        print("Marks:", details['marks'])
        print("Total marks:", details['total_marks'])
        print("Percentage:", round(details['percentage'], 2))
        print("Grade:", details['grade'])
        print("---------------------")


def search_student():
    if not students:
        print("No student records found!")
        return

    roll_number = input("Enter roll number to search: ")

    if roll_number in students:
        details = students[roll_number]
        print("Roll number:", roll_number)
        print("Student name:", details['student_name'])
        print("Marks:", details['marks'])
        print("Total marks:", details['total_marks'])
        print("Percentage:", round(details['percentage'], 2))
        print("Grade:", details['grade'])
    else:
        print(f"No student found with roll number {roll_number}.")


def find_topper():
    if not students:
        print("No student records found!")
        return

    topper_name = ""
    highest_marks = -1
    topper_grade = "A"
    topper_marks = []

    for roll, details in students.items():
        if details['total_marks'] > highest_marks:
            highest_marks = details['total_marks']
            topper_name = details['student_name']
            topper_grade = details['grade']
            topper_marks = details['marks']

    print("Topper:", topper_name)
    print("Total Marks:", highest_marks)
    print("Marks:", topper_marks)
    print("Grade:", topper_grade)


def menu():
    while True:
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Find topper")
        print("5. Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        if choice == 1:
            add_student()
        elif choice == 2:
            view_all_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            find_topper()
        elif choice == 5:
            print("Thank you for using this.")
            break
        else:
            print("Invalid choice")


menu()