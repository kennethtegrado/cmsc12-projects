'''
Exercise 3: Arithmetic Operations

CMSC 12 | Course

Submitted to:
Professor Aragones

Submitted by:
TEGRADO, Kenneth Renz A.
'''
'''
The purpose of this program is to create a tool that will make use of two positive integers inputted by the users through:
1. Summation (computes the summation of squares of all even integers from 1 to x)
2. Box (prints NxN box pattern using *)
3. Average (computes the average of odd integers from 1 to x)

Note that:
> x must be an even integer
> y must be an odd integer
> all functions must accept an INPUT PARAMETER and must RETURN A VALUE
'''


def isEven(num1):  # define a function named isEven and place a single input parameter
    # use this function to check whether a number is an EVEN integer
    # a single input is the only needed parameter because in the condition, the first integer should be the ONLY EVEN INTEGER
    # function will return True if the number placed modulo 2 is equal to 0, otherwise False
    return (num1 % 2 == 0)
    # if the boolean value returned by this function is True then it means that the number is indeed an EVEN integer
    # if the boolean value returned by this function is False then it means that the numver is not an EVEN integer


def isOdd(num2):  # define a function named isOdd and place a single input parameter
    # use this function to check whether a number is an ODD integer
    # a single input is the only needed parameter because in the condition, the second integer should be the ONLY ODD INTEGER
    # function will return True if number placed modulo 2 is not equal to 0 , otherwise False
    return (num2 % 2 != 0)
    # if the boolean value returned by this function is True then it means that the number is an ODD integer
    # if the boolean value returned by this function is False then it means that the number is not an ODD integer


def isPositive(num1, num2):  # define a function named isPositive and place two input parameter
    # use this function to check whether two numbers are POSITIVE integers
    # return True if both integers placed are positive numbers, otherwise False
    return (num1 > 0) and (num2 > 0)
    # if the boolean value returned by this function is True then both integers are POSITIVE numbers
    # if the boolean value returned by this function is False then one or both of the integers are NEGATIVE numbers


def sumSquares(ranges):  # define a function named sumSquares and place a single input parameter
    # use this function to compute for the sum of the squares of even numbers ranging from 1 to the integer placed by the user
    sum = 0  # create a variable to store the sum of the squares of the number; temporarily set it to 0
    # iterate between the elements starting from 1 up to the value of the ranges parameter
    for num in range(1, ranges + 1):
        # add a +1 to the parameter since for loops only includes the element before the end value
        if isEven(num):  # condition to check if the num variable is an EVEN integer
            # if the isEven() function returns a True value then the program will do the operations under this statement
            sum += num ** 2  # add the value of num raised to 2 to the value of the sum variable
    return sum  # return the value of the sum after the for loop is done to the program


def createBox(num):  # define a function named createBox with a single input parameter
    # this function allows us to create a box depending on the value of the second integer
    boxHolder = ''  # emptry string named boxHolder that will store the string value for making the box
    for x in range(num):  # iterate depending on the value of the second integer
        for y in range(num):  # iterate for each x element and the number of iteration is still based on the value of the second integer
            boxHolder += '* '  # add a '* ' character with a space after to the boxHolder empty string
        # add a '/n' after iterating an x element to produce a new line for another iteration
        boxHolder += '\n'
    # return the value of string containing the syntax for generating a box to the program
    return boxHolder


def oddAverage(num):  # define a function named oddAverage with a single input parameter
    # this function allows us to compute for the average of all odd integers between 1 and the first integer placed by the user
    sumOdd = 0  # create a variable sumOdd to store the sum of all odd integers between 1 and the first integer, set temporary value to 0
    totalNumber = 0  # create variable totalNumber to store the total number of odd integers between 1 and first integer, set temporary value to 0
    # create a variable average to store the computed value of (sumOdd / totalNumber), set temporary value to 0
    average = 0
    # iterate between the elements starting from one until the end value with an additional 1 in it
    for i in range(1, num + 1):
        # note that functions only iterates until the number before the end value, add a +1 so that the end value will be included
        if isOdd(i):  # condition to check if the i variable is an odd number through the isOdd() function
            # if isOdd(i) returns a True value then the the condition is met so the statement will do the following:
            sumOdd += i  # add the value of i to sumOdd if it is an odd integer
            totalNumber += 1  # add one for everytime the condition is true to update the number of Odd integer between the sequence
    # compute for the average by dividing the sumOdd by totalNumber then store its value to average variable
    average = sumOdd / totalNumber
    return average  # return the value of average to the program


def mainProgram():  # define a function named mainProgram
    # this function will be used to ask for user input then relay the values to the program using a tuple
    firstNum = int(input('Enter value for x: '))
    # ask for user input then convert the string object to an int
    # after the value was converted to an int, store it to a variable named firstNum
    secondNum = int(input('Enter value for y: '))
    # ask for user input for a second time then convert the string object to an int
    # after the value was converted to an int, store it to a variable named secondNum
    return firstNum, secondNum  # return the value of firstNum and secondNum to the program
    # note that a tuple is returned when a function returns two or more values back to the program
    # this object is immutable and cannot be modified outside the program
    # despite this, tuples can be unparsed and indexed which is still considered conventional for handling data from functions


# define a function named actionChecker that can accept two input parameters
def actionChecker(num1, num2):
    # this function is used to validate whether the integers gathered from the mainProgram() function follows the condition needed by
    # the program to work
    if isEven(num1) and isOdd(num2) and isPositive(num1, num2):
        # condition to check whether the inputs of the user follows all the condition of the program
        # the first integer should be even, the second integer should be odd, and both integers should be positive for this condition to work
        return True
        # the function should return a True boolean value if the condition is met
        # this True value will be used to determine if the program should proceed with the next step
    else:  # condition to set what the program will do if the user's input did not meet any of the condition set by the program for the integers
        # if the values placed did not meet any of the condition set by the program, this condition will check what conditions were not met
        # condition to check if both integers are positive numbers by calling the isPositive() function
        if not isPositive(num1, num2):
            # the statement will only activate if the condition is true that's why we need to use the not operator
            # use the not operator so that when the boolean value of isPositive() is false, it will become true and vice versa
            # prompt the user that the input should be both POSITIVE integers
            print('x and y must be both POSITIVE integers!')
        if not isEven(num1):  # condition to check whether the first input of the user is an EVEN integer through the isEven() function
            # the statement will only activate if the condition is true that's why we need to use the not operator
            # use the not operator so that when the boolean value of isEven() is false, it will become true and vice versa
            print('x must be an EVEN integer!')
        if not isOdd(num2):
            # the statement will only activate if the condition is true that's why we need to use the not operator
            # use the not operator so that when the boolean value of isOdd() is false, it will become true and vice versa
            print('y must be an ODD integer!')
        print()  # create a line space for visual purposes
        return False
        # the function should return a False boolean value if the condition is not met
        # this False value will tell the program to stop with the current step and there is no need to continue


def showMenu():  # define a new function that will be named as menu
    # when naming functions, follow the rule for naming variables
    # avoid using general naming convention such as "x" or "y" so people can easily replicate and understand the program
    # print a statement to show the operations available
    print("Please choose from the following:\n 1. Summation\n 2. Box\n 3. Average\n 0. Exit")
    # ask for user input using input() function
    choice = input("Enter your choice: ")
    return choice  # sends the value of the choice out of the function to our program so that we can decide what we will do


# Start of the Program

# Using the print() function, create a short introduction about what is the program and a loading-like prompt
print()
print('Welcome to the Two-Integer Operator Program')
print('initializing program...')
print()

# Let's start asking for the input from the user by calling the mainProgram() function we've created
firstNumber, secondNumber = mainProgram()
# the line above allows us to unparse the tuple returned by the mainProgram() to two variables while calling it at the same time
# the mainProgram() function we've created returns a tuple which can be unparsed by assigning a variable correspondingly
print()  # create a line space after the first function

# Let's check whether the numbers placed by the user corresponds with the condition below by calling the actionChecker() function
'''
The numbers placed by the user should follow the following conditions:
> first number must be an even integer
> second number must be an odd integer
> any of the numbers cannot be a negative integer

By checking the condition, the actionChecker() function should check whether the conditions are met and return a value that the program 
can easily interpret
'''
action = actionChecker(firstNumber, secondNumber)
# create a variable to store the boolean values return by the actionChecker() function
# set the parameters for the actionChecker() function using the variables we assigned to unparse the tuple from the mainProgram() function

# Let's create a while loop if the user's input met the condition we set by using the action variable
while action:  # a loop that allows us to continuously ask the user what operation they want to achieve from using the program
    # if the actionChecker() function returned a True boolean value then this loop will work
    # if the actionChecker() function returned a False boolean value then this loop will not work
    userChoice = showMenu()
    print()  # allows us to create a line space after the user chose  a operator
    # call the showMenu() function then store the returned value to the userChoice variable so the program can decide what will it do
    if userChoice == '1':  # condition that will check if the user chose the first option which is summation
        # if the condition is True, then the program should do the operation for option 1
        # call the sumSquares() function then set the parameter to the value of the first integer
        sum = sumSquares(firstNumber)
        # store the value of the summation in the sum variable so that we can put a prompt telling what the value is
        print('The sum of the squares of all even integers from 1 to',
              firstNumber, 'is', sum)  # prompt to tell us what the value is
        print()  # add a line space after this instance of the loop
    elif userChoice == '2':  # condition that will check if the user chose the second option which is to create a box
        # if the condition is True, then the program should do the operation for option 2
        # call the createBox() function then set the parameter to the value of the second integer
        box = createBox(secondNumber)
        # store the returned value in another variable that we will be calling box so we can print it
        print(box)
    elif userChoice == '3':  # condition that will check if the user chose the second option which is to find the average of the odd integers
        # if the condition is True, then the program should do the operation for option 3
        # call the oddAverage() function then set the parameter to the value of the first integer
        average = oddAverage(firstNumber)
        # then store the returned value of the oddAverage() function in the average variable so that we can print the value
        print('The average of odd integers from 1 to',
              firstNumber, 'is', average)
        print()  # add a line space after this instance of the loop
    elif userChoice == '0':  # condition that will check if the user chose the fourth option which is to exit from the program
        # if the condition is True, then the program should do the operation for option 4 and exit the program
        # prompt to inform the user that the program is now exiting
        print('Goodbye! Have a great day!')
        print()  # promp to make a line space for visual purposes
        break  # this operator allows us to stop the loop which will in turn stop the program
    else:  # condition that will check if the user did not place the correct option
        # if the condition is True, then we should inform the user that their choice is Invalid
        print('Invalid Option! \nPlease try again...')
        print()  # add a line space after this instance of the loop

# End of the Program
