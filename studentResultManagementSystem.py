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

    while True:
        student_name = input("Enter student name : ").strip()
        if student_name == "":
            print("Student name should not be empty!")
            continue
        break
    subjects = ['Physics', 'Chemistry', 'Mathematics']
    marks =[]
    for sub in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {sub} out of 100 : "))
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Enter a number only.")
        
            

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
    students[roll_number] = student
def view_all_students():
    if len(students) == 0:
        print("There is no student in the record!")
        return
    
    for roll ,details in students.items():
        print("Roll number : " , roll)
        print("Student name : ",details['student_name'])
        print("Marks : ", details['marks'])
        print("Total marks : ", details['total_marks'])
        print("Percentage : " , round(details['percentage'] , 2))
        print("Grade : " , details['grade'])
        print("---------------------")


def search_student():
    if len(students) == 0:
        print("There is no student in the record!")
        return
    
    roll_number = input("Enter roll number to search : ")
    if roll_number in students:
        details = students[roll_number]
        print("Roll number : " , roll_number)
        print("Student name : ",details['student_name'])
        print("Marks : ", details['marks'])
        print("Total marks : ", details['total_marks'])
        print("Percentage : " , details['percentage'])
        print("Grade : " , details['grade'])
    else:
        print(f"With this {roll_number} roll number there is no student in our record! ")
def find_topper():
    if len(students) == 0:
        print("There is no student in the record!")
        return

    topper_name = ""
    highest_marks = -1
    topper_grade = 'A'
    topper_marks = []

    for roll, details in students.items():
        if details['total_marks'] > highest_marks:
            highest_marks = details['total_marks']
            topper_name = details['student_name']
            topper_grade = details['grade']
            topper_marks = details['marks']




    print("Topper:", topper_name)
    print("Total Marks : " , highest_marks)
    print("Marks : ", topper_marks)
    print("Grade : " , topper_grade)
    


    
def menu():
    while True:
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Find topper")
        print("5. Exit")
        while True:
            try:
                choice = int(input("Entere your choice : "))
                break
            except ValueError:
                print("Invalid input! Please enter number only.")
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