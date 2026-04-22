# while loop
# password = "login@123"
# chosen_password = ""
# while chosen_password != password:
#     chosen_password = input("Enter password:")
#     print("Incorrect password, try again!")
# print("Successfully logged in!")

i = 1
while i<6:
    print(i)
    i+=1


# for loop
for i in range(1,6):
    print(i)

name = "akshaye"
for letter in name:
    print(letter)

fruits = ["apple", "mango","chikoo"]
for fruit in fruits:
    print(fruit)


# nested loops
for x in range(1,6):
    for y in range(1,6):
        print(f"{x} * {y} = {x*y}")
    print("--------------")
