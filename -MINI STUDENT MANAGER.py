students = {}
choice = ""
while True:
    choice = input("""
    1. Add Student
    2. View Students
    3. Search Student
    4. Exit
    """)
    if choice == "1":
        stud_id = int(input("Enter student id:"))
        stud_name = input("Enter student name:")
        students[stud_id] = stud_name
    elif choice == "2":
        for id in students:
            print(f"{id} : {students[id]}")
    elif choice == "3":
        stud_id = input("Enter student id to search:")
        if stud_id in students:
            print(students[stud_id])
        else:
            print("Not found")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
