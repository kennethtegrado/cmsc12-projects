'''
Exercise 7: Recursion

CMSC 12 | Course

Submitted to:
Professor Aragones

Submitted by:
TEGRADO, Kenneth Renz A.
'''

'''
The purpose of the program is to create an application that can add and subtract the contents of two one-dimensional vectors.
It should also be able to get the summation of a chosen vector

Our application should be able to do the following:
> Ask a user about the lengths of vectors then create a list object with elements placed by the user
> It must show a menu after the user placed an input 
> Choices are as follows:
    - Add Vectors(choosing this will make a new list object that contains the sum of elements of the two lists with the same index)
    - Subtract Vectors(choosing this will make a new list object that contains the difference of elements of the two lists with the same index)
    - Get Summation(adds all the elements of a list)

Note that all of these functions must be done recursively
'''


# All of the functions of the program

def menu():  # define a new user function named menu
    # use this function to prompt all the functions of the program
    print(
        'Welcome to the recursion program!\nPlease choose a function below for the program to work\n [1] Add Vectors\n [2] Subtract Vectors\n [3] Get Summation')
