'''
Exercise 2: Iterative Statements

CMSC 12 | Course

Submitted to:
Professor Aragones

Submitted by:
TEGRADO, Kenneth Renz A.
'''

'''
The purpose of this program is to create a tool where we can find the sum of the odd and even of the numbers between the given integers 
gathered from the user. 

We need to note that equal numbers is not allowed! Assume that all inputs are positive integers!
'''

# Let's Create a Brief Introduction using the print() method
print("Welcome to the Odd & Even Calculator")
print("Have fun with using our program!")
print()
print("...")
print()

# Let's Ask for the two Integers where we will get the range of the sum of the odd and even
firstInteger = int(input("Enter an Integer in this line: ")) #ask for an integer then convert string object to integers
secondInteger = int(input("Enter another Integer in this line: ")) #ask for an integer then convert string object to integers
# Use input() method to ask for an input from the user
# Use the print() method to create a space between the output and the input
print()
'''
Note that when naming variable, avoid using general names such as x, y, or z. Using general names for variables
might seem efficient when working alone, however, working with organizations generally help people to easily replicate
and understand our program when we use specific names fitted for the right purpose.

Also take note that I used the int() method to enclose the input() method since we need to convert a string to an integer.
When we use input, may it be a number or an alphabet, it will always return a string object which cannot be processed mathematically.
'''

# Let's create a conditional statement that would check whether the first integer is bigger than the second integer and vice versa
if firstInteger > secondInteger:
    # If the first integer is bigger than the second integer then we swap their values using the procedure below
    firstInteger, secondInteger = secondInteger, firstInteger #the first integer will be the second integer's value and vice versa
# If the second integer is bigger than the first integer then we don't do anything

# Let's create some new variables for the loop that we are going to make
evenSum = 0 #create a variable to store the sum of the even numbers between the first and second integers, set 0 as the value
oddSum = 0 #create a variable to store the sum of the odd numbers between the first and second integers, set 0 as the value

'''
    These conditional statements were created to check whether the integers placed are equal or not
    If the integers placed are not equal then we will find the sum and even of the numbers between the integers (inclusive)
    If the integers placed are equal then we will terminate the program and display a prompt that says "The two integers cannot be equal."
'''
if firstInteger != secondInteger: #check if the integers are not equal using the != relational logic
    for num in range(firstInteger, secondInteger + 1): #iterate between the elements from the first and second integer
        '''
        This For Loop iterate between the numbers from the first integer and the second integer
        We used the range() method to set the boundaries of the numbers that we are going to iterate in the For Loops
        Since we need the program to be inclusive, we must add a +1 to the second variable that we included in the range() method
        The range(start, end) method does not include the end value when iterating that's why we need a +1
        '''
        if num % 2 == 0: #use modulus to check if the number is an even number 
            #if the number is divided by 2 and the remainder is 0 then it is always an even number
            #use modulus to determine the value of the remainder of a number when we divide it with another number
            evenSum += num #we add the number if it is an even number to our evenSum variable 
        else: #if the number did not meet the condition above then it is automatically an odd number
            oddSum += num #add the number to the oddSum variable if it is an odd number
    print("The sum of even numbers from", firstInteger, "to", secondInteger, "is", evenSum)  #print the value of the sum of the even numbers
    print("The sum of odd numbers from", firstInteger, "to", secondInteger, "is", oddSum)  #print the value of the sum of the odd numbers
else: #if both integers are equal then do this condition
    print("The two integers cannot be equal.") #print this statement if the integers are equal
print()
print("...")
print("Thank you for using our program") #tell user that the program is done
print()