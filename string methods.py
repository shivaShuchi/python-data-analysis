
# Simulate Gmail Functionality
email = input("Enter your Email ID: ")
format_email = email.lower().strip()
print(f"Original Email: {email}")
print(f"Formatted Email: {format_email}@gmail.com")

# PAN Simulation
pan = input("Enter your PAN ID: ")
if len(pan) == 10 and pan.isalnum() :
    format_pan = pan.upper()
    print(f"Original PAN: {pan}")
    print(f"Formatted PAN: {format_pan}")
else:
    print("Invalid PAN")

# Phone ISD Scenario
mobile_no = input("Enter your phone number with ISD:")
if mobile_no.startswith("+91"):
    print("Calling India Number Charged In Rupees")
elif mobile_no.startswith("+1"):
    print("Calling USA Number Charged In Dollars")
elif mobile_no.startswith("+33"):
    print("Calling France Number Charged In Euros")
else:
    pass

# Email Synchronization
source_email = input("Enter Your Source Email ID: ")
dest_email = input("Enter Your Destination Email ID: ")
if source_email.endswith("@gmail.com") and dest_email.endswith("@gmail.com"):
    print("Email Synchronization Started")
else:
    print("Email Synchronization Failed")

# Simulate CSV data
emp1_data = "Damon Salvatore,damon@gmail.com,32,Paris,Data Analyst"
emp1_data_list = emp1_data.split(",")
print(f"Name: {emp1_data_list[0]}")
print(f"Email ID: {emp1_data_list[1]}")
print(f"Age: {emp1_data_list[2]}")
print(f"City: {emp1_data_list[3]}")
print(f"Job Role: {emp1_data_list[4]}")



s = "mississippi"
print(s.count("iss", 2, 8))

s = "  PyThOn ProGRamMiNg  "
s = s.strip().swapcase().replace(" ", "")
print(s)

s = "Hello123World"
print(s.isalnum(), s.isalpha(), s.isdigit())

s = "data-science-python"
print(s.split("-", 1)[1].upper()) # new knowledge

s = "banana"
print(s.replace("a", "A", 2).find("A"))

s = "PythonIsFUN"
print(s.lower().startswith("python"), s.endswith("FUN"))

s = "  interview preparation  "
print(len(s.strip().title().split()))

s = "aaaBBBcccDDD"
print(s.swapcase().count("b"))

s = "Learn@Python#2025"
print("@" in s, s.replace("@", "").replace("#", "").isalnum())

s = "one,two,,three,"
print(len(s.split(","))) # notice



# SENTENCE WORD COUNTER
sentence = " Python makes coding easy "
print(len(sentence.strip().split()))

# LOG MESSAGE ANALYZER
line = "ERROR 404 Page Not Found"
part = line.split(" ")
print(f"Error Type:{part[0]}")
print(f"Error Code:{part[1]}")
print(f"Error Message:{" ".join(part[2:]).lower()}")

# FILE EXTENSION IDENTIFIER
file = "resume.final.v2.PDF"
extension = file.split(".")[-1].lower()
print("Extension:",extension)
if extension in ["pdf","doc","txt"]:
    print("Valid extension: True")
else:
    print("Valid extension: False")

# URL CLEANER
url = "https://www.example.com/"
domain_name = url.split("/")[2].replace("www.", "")
print(domain_name)

# CUSTOMER REVIEW FILTER
review = "This product is not good at all"
formatted_review = review.lower()
if "not" in formatted_review or "bad" in  formatted_review or "worst" in formatted_review:
    print("Negative Review")
else:
    print("Positive Review")

# CHAT MESSAGE SANITIZER
msg = "Hey!!! Are you free???"
while "!!" in msg or "??" in msg:
    msg = msg.replace("!!", "!").replace("??", "?")
msg = msg.strip().capitalize()
print(msg)

# SEARCH QUERY NORMALIZER
query = "  Best   Python   Course  "
words = query.strip().lower().split()
normalized_query = "-".join(words)
print(normalized_query)
