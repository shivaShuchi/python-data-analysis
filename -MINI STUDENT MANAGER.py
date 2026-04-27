import time
import json

username = "sati"
password = "4321"

for i in range(3):
    user = input("Enter user name:")
    passwd = input("Enter password:")
    if user == username and passwd == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password!")
else:
    print("Too many attempts, exiting...")
    exit()

print("MINI STUDENT MANAGER".center(100,"-"))

try:
    with open("students.json","r") as f:
        students = json.load(f)
except:
    students = {}
choice = ""

def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f)

while True:
    choice = input("""
    1. Add Student
    2. Update Student
    3. Delete Student
    4. Search Student
    5. View Students 
    6. Exit 
    """).strip()
    if choice == "1":
        print("Your choice: Adding Student")
        stud_id = input("Enter student id:")
        if stud_id in students:
            print("Student already exists!")
        else:
            stud_name = input("Enter student name:")
            students[stud_id] = stud_name
            save_data()
            print("Student added successfully!")
    elif choice == "2":
        print("Your choice: Updating Student")
        stud_id = input("Enter student id to update:")
        if stud_id in students:
            stud_name = input("Enter updated student name:")
            students[stud_id] = stud_name
            save_data()
            print("Student updated successfully!")
        else:
            print("Not found")
    elif choice == "3":
        print("Your choice: Deleting Student")
        stud_id = input("Enter student id to delete:")
        if stud_id in students:
            students.pop(stud_id)
            save_data()
            print("Student deleted successfully!")
        else:
            print("Not found")
    elif choice == "4":
        print("Your choice: Searching Student")
        stud_id = input("Enter student id to search:")
        if stud_id in students:
            print(students[stud_id])
        else:
            print("Not found")
    elif choice == "5":
        print("Your choice: Viewing Students")
        if not students:
            print("No students available")
        else:
            print(f"Total students: {len(students)}")
            for stud_id, stud_name in students.items():
                print(f"{stud_id} : {stud_name}")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
    print("*"*40)
    time.sleep(2)
