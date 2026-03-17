import json
students = {}

# ---------- HELPER FUNCTIONS ----------
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
def get_valid_marks():
    subjects = ['Physics', 'Chemistry', 'Mathematics']
    marks = []

    for sub in subjects:
        while True:
            try:
                mark = int(input(f"Enter mark for {sub} out of 100: "))
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Enter a number only.")
    return marks


def display_student(roll, details):
    print("Roll number:", roll)
    print("Student name:", details['student_name'])
    print("Marks:", details['marks'])
    print("Total marks:", details['total_marks'])
    print("Percentage:", round(details['percentage'], 2))
    print("Grade:", details['grade'])
    print("---------------------")

def generate_roll_number():
    if not students:
        return '1'
    highest_roll = max(int(roll) for roll in students.keys())
    return str(highest_roll + 1)

def save_students():
    with open ("students.json" , "w") as file:
        json.dump(students , file)

def load_students():
    global students
    try:
        with open ("students.json" , "r" ) as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}


# ---------- MAIN FUNCTIONS ----------
def add_student():
    
    roll_number = generate_roll_number()
    print("Assigned roll number:", roll_number)  

    while True:
        student_name = input("Enter student name: ").strip()
        if student_name == "":
            print("Student name should not be empty!")
            continue
        break
    marks = get_valid_marks()
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
    save_students()
    print("Student record added successfully!")
    print("---------------------")


def view_all_students():
    if not students:
        print("No student records found!")
        return

    for roll, details in students.items():
        display_student(roll, details)


def search_student():
    if not students:
        print("No student records found!")
        return

    roll_number = input("Enter roll number to search: ")

    if roll_number in students:
        details = students[roll_number]
        display_student(roll_number, details)
    else:
        print(f"No student found with roll number {roll_number}.")


def find_topper():
    if not students:
        print("No student records found!")
        return

    topper_roll = ""
    topper_details = {}
    highest_marks = -1

    for roll, details in students.items():
        if details['total_marks'] > highest_marks:
            highest_marks = details['total_marks']
            topper_roll = roll
            topper_details = details

    print("Topper Details")
    print("---------------------")
    display_student(topper_roll, topper_details)


def update_student():
    if not students:
        print("No student records found!")
        return

    roll_number = input("Enter roll number to update details: ")

    if roll_number not in students:
        print("Student not found!")
        return

    update_choice = input("What do you want to update? (name/marks): ").strip().lower()

    if update_choice == "name":
        while True:
            new_name = input("Enter updated name: ").strip()
            if not new_name:
                print("Name cannot be empty!")
                continue
            break
        students[roll_number]['student_name'] = new_name
        save_students()
        print("Name updated successfully!")

    elif update_choice == "marks":
        new_marks = get_valid_marks()

        students[roll_number]['marks'] = new_marks
        total_marks = calculate_total(new_marks)
        student_percentage = calculate_percentage(total_marks, new_marks)
        student_grade = calculate_grade(student_percentage)

        students[roll_number]['total_marks'] = total_marks
        students[roll_number]['grade'] = student_grade
        students[roll_number]['percentage'] = student_percentage

        save_students()

        print("Marks updated successfully!")

    else:
        print("Invalid update choice!")


def delete_student():
    if not students:
        print("No student records found!")
        return

    roll_number = input("Enter roll number to delete student: ")

    if roll_number not in students:
        print("Student not found!")
        return

    details = students[roll_number]
    display_student(roll_number, details)

    confirm = input("Are you sure you want to delete this student? (y/n): ").strip().lower()

    if confirm == "y" or confirm == "yes":
        students.pop(roll_number)
        save_students()
        print("Student with above details deleted.")
    else:
        print("Deletion cancelled.")


def menu():
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Find topper")
        print("5. Update student records")
        print("6. Delete student records")
        print("7. Exit")

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
            update_student()
        elif choice == 6:
            delete_student()
        elif choice == 7:
            print("Thank you for using this.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

load_students()
menu()