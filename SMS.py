#student management system
students = []
while True:
    print("\n\nwelcome to student management system", "\n")
    print("press 1 to add student ")
    print("press 2 to delete student")
    print("press 3 to search student")
    print("press 4 to check total enrolled students")
    print("press 5 to exit \n")
    choice = int(input("enter your choice: "))
    if choice == 1:
        student = {}
        student["name"] = input("enter name: ")
        student["father name"] = input("enter father name: ")
        student["phone number"] = input("enter phone number: ")
        student["age"] = input("enter age: ")
        students.append(student)
        print("you added student", student)
        print("list of total student is", students)
    elif choice == 2:
        a = input("enter the name of studnt you want to delete: ")
        for student in students:
            if student["name"].lower() == a.lower():
                s
            print(students)
    elif choice == 3:
        b = input("enter the name you want to search: ")
        for student in students:
            if student["name"].lower() == b.lower():
                print("yes ",b , "is our student")
    elif choice == 4:
        print("total enrolled students are", len(students))
    elif choice == 5:
        break
    else:
        print("you entered invalid choice")



   