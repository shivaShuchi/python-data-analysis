# CRUD APP

system_info = ("Company Name : Edify Technologies",
               "Software Name : Student Management System",
               "Version : v1")
for info in system_info:
    print(info)
print("*" * 120)

stud_ids = []
stud_names = []
stud_scores_list = []
stud_skills_list = []

print("MENU".center(120))
print("""
PRESS 1 TO ADD STUDENT
PRESS 2 TO MODIFY STUDENT
PRESS 3 TO DELETE STUDENT
PRESS 4 To LIST STUDENT
""")
choice = input("Your Choice : ")


if choice == "1":
    print("User wants to add a student")
    while True:
        stud_id = input("Enter Student ID : ")
        if stud_id in stud_ids:
            print("ID Already Exists")
        else:
            stud_ids.add(stud_id)
            break
    stud_name = input("Enter Student Name : ")
    stud_name = stud_name.title()
    stud_names.append(stud_name)
    stud_scores = []
    while True:
        stud_score = input("Enter Score or Type Done : ")
        stud_score = stud_score.lower()
        if stud_score == "done":
            break
        elif int(stud_score) >= 1 and int(stud_score) <= 100:
            stud_scores.append(stud_score)
        else:
            print("Score should be between 1 and 100:")
    stud_scores_list.append(stud_scores)
    stud_skills = set()
    while True:
        stud_skill = input("Enter Skill or Type Done : ")
        stud_skill = stud_skill.lower()
        if stud_skill == "done":
            break
        else:
            stud_skills.add(stud_skill)
    stud_skills_list.append(stud_skills)

print(stud_ids)
print(stud_names)
print(stud_scores_list)
print(stud_skills_list)

print("*" * 120)
admin_info = ("Admin Contact : 9090813132",
               "Admin Email : admin@edify.com")
for info2 in admin_info:
    print(info2)
