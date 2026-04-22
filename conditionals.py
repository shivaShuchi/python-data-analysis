# if
num = int(input("choose number between 1-10:"))
if num == 5:
    print("correct")


# if else
n = int(input("enter a number:"))
# if n % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# short hand if else
print("even number") if n % 2 == 0 else print("odd number")


# if elif else
score = int(input("enter score under 100:"))
if score > 90:
    print("First")
elif score > 80:
    print("Second")
elif score > 70:
    print("Third")
else:
    print("Participated")


# match case
grade = input("Enter grade:")
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Need to Improve")
    case "D":
        print("Fail")
    case _:
        print("Invalid Grade")


# nested conditionals
age = int(input("Enter your age:"))
if age>18:
    id = input("Do you have voter id?")
    if id == "Yes":
        print("You can vote!")
    else:
        print("Register for voter id")
else:
    print("You cannot vote!")
