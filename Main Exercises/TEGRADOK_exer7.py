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


def listMaker():  # define a new user function named listMaker
    # use this function to create two lists with the length based on the choice of the user
    # init length with the value based on the user input
    length = int(input("How many items to be placed in the list: "))
    if length > 0:
        print('\nEnter Contents for List 1')
        # init listOne with value equal to the object returned by the list1(function)
        listOne = listFirst(length)
        print('\nEnter Contents for List 2')
        listTwo = listSecond(length)
        # return the value of list1 and list2 back to the main program inside a tuple for unparsing
        return [listOne, listTwo, length]
    else:
        print('\nNumber placed cannot be used as a basis for the lengths of the sequence of the two lists!\nPlease try again!\n')


def listFirst(length):  # define a new user function named listFirst with length parameter
    # use this recursive function to create a list object with a number of elements on a sequence based on the length parameter
    if length <= 0:  # base case
        # if length is less than or equal to 0 then return an empty list to recursive function
        return []
    # init element with value equal to user input
    element = int(input('Enter a number for List 1: '))
    return [element] + listFirst(length - 1)  # recursive case
    # wrap the [element] in braces to create a list object
    # use the + operator to concatenate the list returned by the recursive case
    # deduct 1 to our length to init a recursive step


def listSecond(length):  # define a new user function named listSecond with length parameter
    # use this recursive function to create a list object with a number of elements on a sequence based on the length parameter
    if length <= 0:  # base case
        # if length is less than or equal to 0 then return an empty list to recursive function
        return []
    # init element with value equal to user input
    element = int(input('Enter a number for List 2: '))
    return [element] + listSecond(length - 1)  # recursive case
    # wrap the [element] in braces to create a list object
    # use the + operator to concatenate the list returned by the recursive case
    # deduct 1 to our length to init a recursive step


def menu():  # define a new user function named menu
    # use this function to prompt all the functions of the program
    print(
        '\nWelcome to the recursion program!\nPlease choose a function below for the program to work\n [1] Add Vectors\n [2] Subtract Vectors\n [3] Get Summation\n [4] Exit\n')
    # init choice to hold the function of choice of user
    choice = input("Enter your choice here: ")
    return choice  # using the return method, send the value of the choice variable back to the main program


# define a new user function named addVectors and set the parameters to l1, l2, length, and counter
def addVectors(l1, l2, length, counter):
    # set the default value of counter to 0 so our indexing will always start with 0
    # use this function to determine the sum of each elements of the two list objects
    if counter >= length:  # base case
        # if the counter is now greater than the length, it means that we can no longer use indexing to find an element in a sequence
        # hence, we need to return an empty list to end the recursive case without affecting our output
        return []  # return empty list if the recursion reached its base case
    # recursive case
    return [l1[counter] + l2[counter]] + addVectors(l1, l2, length, counter + 1)
    # wrapping [l1[counter] - l2[counter]] in braces [] creates a list object then using the + operator concatenates the new list provided created by the addVector() function
    # every time the addVectors() function is called, 1 is added to the counter to init a recursive step


# define a new user function named subtractVectors and set the parameters to l1, l2, length, and counter
def subtractVectors(l1, l2, length, counter):
    # set the default value of counter to 0 so our indexing will always start with 0
    # use this function to determine the difference of each elements of the two list objects
    if counter >= length:  # base case
        # if the counter is now greater than the length, it means that we can no longer use indexing to find an element in a sequence
        # hence, we need to return an empty list to end the recursive case without affecting our output
        return []  # return empty list if the recursion reached its base case
    # recursive case
    return [l1[counter] - l2[counter]] + subtractVectors(l1, l2, length, counter + 1)
    # wrapping [l1[counter] - l2[counter]] in braces [] creates a list object then using the + operator concatenates the new list provided created by the subtractVector() function
    # every time the subtractVectors() function is called, 1 is added to the counter to init a recursive step


# define a new user function named listChooser with parameters list1 and list2
def listChooser(list1, list2):
    # use this function to return a list that was choosen by user
    print(
        'Please choose a list you wish to add:\n [1] List 1\n [2] List 2\n [3] Go Back to Menu\n')
    # init choice with value chosen by user
    choice = input('Enter your choice here: ')
    if choice == '1':  # return list1 parameter if user chose 1
        return list1
    elif choice == '2':  # return list2 parameter if user chose 2
        return list2
    elif choice == '3':  # return none if user chose 3
        return
    else:  # return none if user chose the wrong input
        return


# define a new user function named summation with paramaters list and length
def summation(list, length):
    # use this function to get the summation of all the elements in the sequence list given the length parameter
    if length <= 0:  # base case
        return 0  # if the length parameter is now less than or equal to 0 then return a value of 0
    return summation(list, length-1) + list[length-1]  # recursive case


def main():  # define a new user function named main
    # use this function to call the entirety of the program
    print('\nPlease follow the instructions to use the program!\n')
    # call list maker to create two arrays
    # init list1, list2, and length that will unparse the values returned by the listMaker() function
    list1, list2, length = listMaker()
    # init counter with value equal to 0 to be used for indexing list objects
    counter = 0
    # While loop to continuously ask the user what they want to do
    while True:
        # init choice with the value returned by the menu() function
        choice = menu()
        if choice == '1':  # if the user chose 1 then call the addVectors() function
            # init sum with the value equal to the returned value of the addVectors() function
            sum = addVectors(list1, list2, length, counter)
            print(f'The sum of the two vectors is {sum}\n')
        elif choice == '2':  # if the user chose 2 then call the subtractVectors() function
            # init difference with the value equal to the returned value of the subtractVectors() function
            difference = subtractVectors(list1, list2, length, counter)
            print(f'The difference of the two vectors is {difference}\n')
        elif choice == '3':  # if user chose 3 then call the summation() function
            # call the listChooser function to ask user which list to choose
            # init chosenList with value equals to the value returned by listChooser function
            chosenList = listChooser(list1, list2)
            # use conditional statements for data validation
            # if instance of the returned value is a list type then call the summation() function
            if isinstance(chosenList, list):
                # init sum with value equals to the returned value by the summation() function
                # set the arguments for the summation() function to chosenList and length variables
                sum = summation(chosenList, length)
                print(f'The sum of your chosen list is {sum}!\n')
            else:  # if instance is not a list then do nothing and continue with the next instance of the loop
                print('\nGoing back to the menu...')
                continue
        elif choice == '4':  # if user chose 4 then break the loop to close the main program
            print('\nThank you for using the program!\nHave a great day!\n')
            break
        else:
            print('\nChoice is invalid! Please try again!\n')


# Start of the main program


main()  # call the main() function to init the whole program
