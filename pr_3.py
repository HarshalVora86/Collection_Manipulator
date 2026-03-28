students = []

print("Welcome to the student data oraganizer!")

while True:
    print("\nSelect an option:")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("\nEnter student details:")
            student_id = int(input("Student id:"))
            name = input("Name:")
            age = int(input("Age:"))
            grade = input("Grade:")
            dob = input("Date of birth (YYYY-MM-DD):")
            subjects = input("Subjects (comma-separated):")

            student = {
                "Student_id" : student_id,
                "Name" : name,
                "Age" : age,
                "Grade" : grade,
                "Date_of_birth" : dob,
                "Subjects" : subjects
            }
            
            students.append(student)
            print("Student added successfully!\n")

        case 2:
            print("\n--- Display all students ---")
            if not students:
                print("No students found.\n")
            else:
                for stu in students:
                    print(
                        f"ID: {stu['Student_id']} |"
                        f"Name: {stu['Name']} |"
                        f"Age: {stu['Age']} |"
                        f"Grade: {stu['Grade']} |"
                        f"Subjects: {stu['Subjects']} |"
                    )
                print()

        case 3:
            print("\nUpdate student information")
            sid = int(input("Enter student ID to update: "))
            found = False

            for stu in students:
                if stu["Student_id"] == sid:
                    found=True

                    print("1. Update name")                    
                    print("2. Update age")                
                    print("3. Update grade")
                    print("4. Update subjects")

                    op = int(input("Enter operation: "))

                    match op:
                        case 1:
                            stu["Name"] = input("Enter new name: ")
                        case 2:
                            stu["Age"] = input("Enter new age:")
                        case 3:
                            stu["Grade"] = input("Enter new grade:")
                        case 4:
                            stu["Subjects"] = input("Enter new subjects:")
                        case _:
                            print("Invalis operation")

                    print("Student information updated!\n")
                    break
                        
            if not found:
                print("Student id not found.\n")

        case 4:
            sid = int(input("Enter student id to delete: "))
            found = False

            for stu in students:
                if stu["Student_id"] == sid:
                    students.remove(stu)
                    found = True
                    print("Student deleted successfully!\n")
                    break           

        case 5:
            print("\n---Offered subjects list---")
            if not students:
                print("No subjects available.\n")
            else:
                for stu in students:
                    print(stu["Subjects"])
                print()
 
        case 6:
            print("Program exit'ed!!!")
            break

        case _:
            print("Invalis choice")