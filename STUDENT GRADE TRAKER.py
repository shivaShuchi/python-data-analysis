# CONTROLS - TASK

while True:
    id = int(input("Enter Your ID: "))

    name = input("Enter Your Name: ")

    response = "yes"
    no_of_subjects = 0
    total_score = 0
    while response == "yes":
        no_of_subjects += 1
        score = int(input(f"Enter Score For Subject {no_of_subjects} (0-100): "))
        total_score += score
        response = input("Do you want to enter with another score (yes/no)? ")

    avg_score = total_score/no_of_subjects

    if avg_score >= 85:
        grade = "A"
    elif avg_score >= 70:
        grade = "B"
    elif avg_score >= 50:
        grade = "C"
    else:
        grade = "D"

    attendance = float(input("Tell attendance percentage(1-100)%: "))
    if attendance >= 75:
        attendance_status = "OK - GOOD ATTENDANCE"
    else:
        attendance_status = "WARNING - LOW ATTENDANCE"

    print("-------------------------")
    print("RESULT")
    print(f"Student ID - {id}")
    print(f"Student Name - {name}")
    print(f"Total Score - {total_score}/{no_of_subjects*100}")
    print(f"Average Score - {avg_score}")
    print(f"Performance Level - {grade}")
    print(f"Attendance Status - {attendance_status}")
    next = input("continue (yes/no)? ")
    if next == "no":
        break
