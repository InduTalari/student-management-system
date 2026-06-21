students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        student_section = input("Enter Student Section: ")
        student_email=input("Enter Student Email: ")
        student_phonenumber=input("Enter Student Phonenumber:")
        student_clgname=input("Enter Clg Name: ")

        student = {
            "id": student_id,
            "name": student_name,
            "section": student_section,
            "email":student_email,
            "phonenumber":student_phonenumber,
            "clgname":student_clgname

        }

        students.append(student)
        print("Student Added Successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Available")
        else:
            for student in students:
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Section:", student["section"])
                print("Email:", student["email"])
                print("Phone Number:", student["phonenumber"])
                print("College Name:", student["clgname"])
                print("-" * 20)

    elif choice == "3":
        user_name = input("Enter Student Name: ")

        found = False

        for student in students:
            if student["name"] == user_name:
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Section:", student["section"])
                print("Email:", student["email"])
                print("Phone Number:", student["phonenumber"])
                print("College Name:", student["clgname"])      
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == "4":
        user_name = input("Enter Student Name to Update: ")

        found = False

        for student in students:
            if student["name"] == user_name:
                new_name = input("Enter New Name: ")
                new_section = input("Enter New Section: ")
                new_email = input("Enter New Email: ")
                new_phonenumber = input("Enter New Phone Number: ")
                new_clgname = input("Enter New College Name: ")

                student["name"] = new_name
                student["section"] = new_section
                student["email"] = new_email
                student["phonenumber"] = new_phonenumber
                student["clgname"] = new_clgname
                print("Student Updated Successfully")
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == "5":
        user_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:
            if student["name"] == user_name:
                students.remove(student)
                print("Student Deleted Successfully")
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")