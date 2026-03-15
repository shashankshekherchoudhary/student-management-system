students = {}
# number_of_students = int(input("How many students are there in your class :"))
def total(marks):
    total_sum = 0
    for mark in marks:
        total_sum += mark
    return total_sum
def percentage(total_marks,marks):
     return (total_marks /len(marks))
def grade(percentagee):
    if percentagee >= 90:
        return "A"
    elif percentagee >= 80:
        return "B"
    elif percentagee >= 70:
        return "C"
    elif percentagee >= 60:
        return "D"
    elif percentagee >= 50:
        return "E"
    else:
        return "Fail"
    
def add_student():
    while True:
        roll_number = input("Enter student roll number : ")
        if roll_number == "":
            print("Roll number cannot be empty!")
            continue
        if roll_number in students:
            print("Roll number already exists!")
            continue
        break


    student_name = input("Enter student name : ")
    subjects = ['Physics','Chemistry','Mathematic']
    marks =[]
    for sub in subjects:
        while True:
            mark = int(input(f"Enter marks for {sub} out of 100 : "))
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100")
                continue
            marks.append(mark)
            break

    total_marks = total(marks)
    percentagee = percentage(total_marks,marks)
    gradee = grade(percentagee)

    student = {
        'student_name' : student_name ,
        'marks' : marks ,
        'total_marks' : total_marks ,
        'percentage' : percentagee ,
        'grade' : gradee 
    }
    students.update({roll_number : student})
def view_all_students():
    for roll ,details in students.items():
        print("Roll number : " , roll)
        print("Student name : ",details['student_name'])
        print("Marks : ", details['marks'])
        print("Total marks : ", details['total_marks'])
        print("Percentage : " , details['percentage'])
        print("Grade : " , details['grade'])


def search_student():
    roll_number = input("Enter roll number to search : ")
    for roll , details in students.items():
        if roll_number == roll:
            print("Roll number : " , roll)
            print("Student name : ",details['student_name'])
            print("Marks : ", details['marks'])
            print("Total marks : ", details['total_marks'])
            print("Percentage : " , details['percentage'])
            print("Grade : " , details['grade'])
            break
    else:
        print(f"With this {roll_number} roll number there is no student in our record! ")
def find_topper():
    if len(students) == 0:
        print("There is no student in the record!")
        return

    topper_name = ""
    highest_marks = -1

    for roll, details in students.items():
        if details['total_marks'] > highest_marks:
            highest_marks = details['total_marks']
            topper_name = details['student_name']


    print("Topper:", topper_name)
    print("Marks : " , details['total_marks'])


    
def menu():
    while True:
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Find topper")
        print("5. Exit")
        choice = int(input("Entere your choice : "))
        if choice == 1:
            add_student()
        elif choice == 2:
            view_all_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            find_topper()
        elif choice == 5:
            print("Thankyou for using this ")
            break
        else:
            print("Invalid choice")
menu()