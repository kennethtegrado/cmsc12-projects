'''
TEGRADO, Kenneth Renz A.
202109799
Module 2 Assessment
Number 2 - Task
'''
def oddList(list): # define new user function named oddList
    '''
    set the parameter to list to explicitly tell our programmer that we are accepting a list object as a parameter
    use this function to create a sequence of odd elements from the list parameter
    we can assume that the list contains all positive numbers but we can also prepare for the worst by adding a data validation 
    on our conditional statement
    '''
  

    listHolder = [] # init listHolder variable with an empty list literal 
    for number in list: #iterate every elements inside the list
        if number % 2 != 0 and number >= 0: # conditional statement
            # check if the current iteration of number is an odd number using the modulo operator and 2
            # check if the current iteration of number is also a positive integer
            listHolder.append(number) # if current iteration of number is an odd number then append it to out listHolder variable
    return listHolder # return the listHolder containing all odd numbers back to the main program


'''
TEGRADO, Kenneth Renz A.
202109799
Module 2 Assessment
Number 1 - Task
'''
def sumOfDigits(integer): # define new user function named sum
    # set the parameter to integer to explicitly tell programmer we are accepting an integer object for this function
    # use this function to find the sum of the digits of a non-negative integer using recursion

    if integer == 0: # base case
        ''' 
        if the value of our integer parameter is 0 then return 0 as a value without calling the sum() function to completely stop
        the recursive steps
        '''
        return 0
    return integer % 10 + sum(integer // 10) # recursive step
    '''
    This recursive step works by first isolating the last digit from the integer using the modulos operator and  floor division operator.
    The last digit of the integer is isolated then its value will be added to the next instance of the recursive step until we reach our
    base case. At the same time, we will use floor division to remove the last digit to our next instance of the recursive step.
    '''


'''
TEGRADO, Kenneth Renz A. 
202109799
Module 2 Assessment
Number 3 - Task
'''
def vowelConsonantCounter(string): # define new user function named vowelConsonantCounter
    # set the parameter to string to explicitly tell our programmer that we are only accepting string as a parameter
    # use this function to count the total number of vowels and consonants in a string
    vowelCharacters = ['a','e','i','o','u']
    consonantCharacters = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowelCounter = 0
    consonantCounter = 0
    for character in string:
        if character.isalpha():
            lowercaseCharacter = character.lower()
            if lowercaseCharacter in vowelCharacters:
                vowelCounter += 1
            else:
                consonantCounter += 1
    return vowelCounter,consonantCounter


list = [2,4,11,6,3,9]

print(oddList(list))
print(sum(2478))