'''
Exercise 1: Variables, Expressions, Sequential, and Selection Statements

CMSC 12 | Course

Submitted to:
Professor Aragones

Submitted by:
TEGRADO, Kenneth Renz A.
'''

'''
The purpose of this program is to create a tool for students to compute their general weighted average (GWA) for ONE SEMESTER
given that they took ONLY FIVE SUBJECTS.
'''

# Let's first create a brief introduction about the program by utilizing Python's print() method
print("Welcome to the GWA Calculator!") 
print("Are you aiming for a Latin Honor?")
print("Let's find out if you got what it takes to receive a Latin Honor!")
print()

# After creating a brief introduction let's start asking for information through a print() method
print("Please input your GRADE and the number of units per SUBJECT")

# Let's ask for their grades and number of units per subject
print("First Subject's Grade:")
firstGrade = float(input("> ")) #ask for grade then convert string object to float
'''
We created a variable with the firstGrade name to contain our value inside our input() method. The input() method allows us to ask for an
input from the user.

Note:
We added a float(input()) method to the input() because we need to convert a string(default object type of an input)
to a float object. We cannot use a string object for mathematical purposes. The float() method allows us to convert a numeric
string object to a float object that allows decimal inputs and can be used for math.

Additional Note:
When naming a variable, we should be specific and clear. This will help people better understand what the variable is used for. 
Avoid using general name such as x, y, and z if you want your variables to be read easily by other people. 
This method of naming may be counter-productive when working on a program alone, but it is very valuable in an organization or a team.
'''

print("Number of Units for this subject:")
firstSubUnits = float(input("> ")) #ask for units then convert string object to float
# Even though units of a subject do not have decimal values, we still used the float() method to convert the string object
# User may input a unit of 1.0 instead of 1 or 2.0 instead of 2 which will cause an error if we used the int() method
# Refer to the comment below the firstGrade variable for more info 

# Let's repeat the process of asking for grades and number of units per subject four more times
# Second Subject
print("Second Subject's Grade:")
secondGrade = float(input("> ")) #ask for grade then convert string object to float
print("Number of Units for this subject:")
secondSubUnits = float(input("> ")) #ask for units then convert string object to float

# Third Subject
print("Third Subject's Grade:")
thirdGrade = float(input("> ")) #ask for grade then convert string object to float
print("Number of Units for this subject:")
thirdSubUnits = float(input("> ")) #ask for units then convert string object to float

# Fourth Subject
print("Fourth Subject's Grade:")
fourthGrade = float(input("> ")) #ask for grade then convert string object to float
print("Number of Units for this subject:")
fourthSubUnits = float(input("> ")) #ask for units then convert string object to float

# Fifth Subject
print("Fifth Subject's Grade:")
fifthGrade = float(input("> ")) #ask for grade then convert string object to float
print("Number of Units for this subject:")
fifthSubUnits = float(input("> ")) #ask for units then convert string object to float

# Let's compute for the GWA by using the (summation of (grades per subject * units per subject)) / (total number of units) formula
totalUnits = firstSubUnits + secondSubUnits + thirdSubUnits + fourthSubUnits + fifthSubUnits 
#store total sum of units to one variable named totalUnits
GWA = ( (firstGrade * firstSubUnits) + (secondGrade * secondSubUnits) + (thirdGrade * thirdSubUnits) + (fourthGrade * fourthSubUnits) + (fifthGrade *fifthSubUnits)) / totalUnits
#variable to store the computed value of the GWA

print("Your GWA is", GWA) 
#print an output to show the GWA of the user
#use comma between objects in a print() method to show that you want the program to print them in a single line with a space included

# Let's create conditional statements to determine what is the corresponding Latin honors of the student based on their GWA
'''
For reference, we should use the corresponding grade range for latin honors used by UP:
> summa cum laude GWA ≤ 1.20
> magna cum laude 1.45 ≥ GWA > 1.20
> cum laude 1.75 ≥ GWA > 1.45
'''
if 1.45 < GWA <= 1.75 :
    # We set the condition where the GWA of the student is higher than 1.45 and less than 1.75 then they are more likely to graduate as a cum laude if they can maintain it
    print("If you can maintain your GWA you can graduate cum laude.")
elif 1.20 < GWA <= 1.45 :
    # We set the condition where the GWA of the student is higher than 1.20 and less than 1.45 then they are more likely to graduate as a magna cum laude if they can maintain it
    print("If you can maintain your GWA you can graduate magna cum laude.")
elif GWA <= 1.20 :
    # We set the condition where the GWA of the student is less than 1.20 then they are more likely to graduate as a summa cum laude if they can maintain it
    print("If you can maintain your GWA you can graduate summa cum laude.")
else:
    # We set the condition where if the user did not meet the GWA required for the latin honors, they have to improve their grades to get a Latin Honors once they graduate
    print("Improve your GWA to receive latin honors.")
print()
print("Thank you for using our Calculator!") #tell user that the program's function is done
print()    