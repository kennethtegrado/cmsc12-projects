'''
TEGRADO, Kenneth Renz A.
202109799
Module 2 Assessment
Number 2 - Task
'''
def oddList(list): # define new user function named oddList
    # set the parameter to list to explicitly tell our programmer that we are accepting a list object as a parameter
    # use this function to create a sequence of odd elements from the list parameter
    # we can assume that the list contains all positive numbers but we can also prepare for the worst by adding a data validation 
    # on our conditional statement

    listHolder = [] # init listHolder variable with an empty list literal 
    for number in list: #iterate every elements inside the list
        if number % 2 != 0 and number >= 0: # conditional statement
            # check if the current iteration of number is an odd number using the modulo operator and 2
            # check if the current iteration of number is also a positive integer
            listHolder.append(number) # if current iteration of number is an odd number then append it to out listHolder variable
    return listHolder # return the listHolder containing all odd numbers back to the main program

list = [2,4,11,6,3,9]

print(oddList(list))