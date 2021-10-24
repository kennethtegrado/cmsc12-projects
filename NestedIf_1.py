print("Gender and Age Identification System")
print("Use F or F for Female while M or M for Male")
gender = input("Enter you gender > ")
age = int(input("Enter your age here > "))

if gender == "F" or gender == "f":
    if 1 <= age <= 17:
        print("Female and Minor")
    elif 18 <= age <= 59:
        print("Female and Adult")
    elif age >= 60:
        print("Female and Senior")
    else:
        print("Female and Invalid")
elif gender == "M" or gender == "m":
    if 1 <= age <= 17:
        print("Male and Minor")
    elif 18 <= age <= 59:
        print("Male and Adult")
    elif age >= 60:
        print("Male and Senior")
    else:
        print("Male and Invalid")
else:
    if 1 <= age <= 17:
        print("Invalid and Minor")
    elif 18 <= age <= 59:
        print("Invalid and Adult")
    elif age >= 60:
        print("Invalid and Senior")
    else:
        print("Invalid and Invalid")

print()
print()
print()
print()

print("Control Structure using Nested If Condition")
year = 