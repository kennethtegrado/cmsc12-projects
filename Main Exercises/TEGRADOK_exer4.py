'''
Exercise 4: Strings and Lists

CMSC 12 | Course

Submitted to:
Professor Aragones

Submitted by:
TEGRADO, Kenneth Renz A.
'''
'''
The purpose of this program is to create a tool where users can place two names and predict what relationship status do you have with them.
This is a program that follows the rules for the game titled 6K’s of relationship.

Note that: 
> This game is for recreational purposes and in no way should be used to dictate what relationship status you should have with that people.
'''

def removeAndCount(user1, user2): #define a function named removeAndCount and add two input parameters
    #use this function to determine common characters found  in the names of the user input
    #when adding values to the parameters to the function, there's no need to consider the order since it will still work no matter the succession
    
    #create a variable named firstUser with a value of an empty string that we can use to store the valid characters of the first parameter
    firstUser = '' 
    #create a variable named secondUser with a value of an empty string that we can use to store the valid characters of the second parameter
    secondUser = '' 

    # Let's create a way to remove characters in the string that are not alphabetical using For loops and the isalpha() funcion
    for letter in user1: #iterate between the characters found in the first parameter
        #consider the parameter as a sequence then use the for loop to iterate on each characters
        if letter.isalpha(): #condition to check if the current character iterated by the loop is an alphabetical character
            #use the isalpha() function to check if the current character is part of an alphabet, it will return a boolean value which can be
            #used for checking conditions
            #if the isalpha() function returned a True boolean value then the condition is met so the program will proceed to the next step
            #otherwise, pass this current iteration and do nothing
            firstUser += letter.lower() #if the character is part of the alphabet then add it to firstUser
            #use the lower() function to convert the character to small case which is vital for checking common characters later on
            #remember that in Python: 'A' != 'a', 'A' == 'A', and 'a' == 'a' 
    for letter in user2: #iterate between the characters found in the second parameter
        #consider the parameter as a sequence then use the for loop to iterate on each characters
        if letter.isalpha(): #condition to check if the current character iterated by the loop is an alphabetical character
            secondUser += letter.lower() #if the character is part of the alphabet then add it to firstUser  
            #use the lower() function to convert the character to small case which is vital for checking common characters later on
            #remember that in Python: 'A' != 'a', 'A' == 'A', and 'a' == 'a'     
            #use the lower() function followed by a strip() function to remove spaces between texts and to convert all characters to lower cases    
    
    # Let's create a way to remove common characters between parameters using For Loops and If Conditional Statements
    firstHolder = '' #variable to store characters in first name that are not found in the second name
    secondHolder = '' #variable to store characters in second name that are not found in the first name
    firstCounter = 0 #variable to count the number of times that a character is added to the firstHolder variable
    secondCounter = 0 #variable to count the number of times that a character is added to the secondHolder variable
    for letter in firstUser: #iterate between the charaters found in the firstUser variable
        if letter not in secondUser: 
            '''
            conditional statement to check if the current character iterated is not found in the characters in the name of the second user
            > if the condition is true, then this statement will add the current character to the firstHolder variable then add 1 to the firstCounter
            variable. Adding one to the firstCounter variable whenever the character is not in the second name will help us determine the number
            of characters in the first user that are not found in the second user.
            > if the condition is false, then this statement will do nothing with the character
            '''            
            firstHolder += letter #if the current character is not found in the second user then add it to the firstHolder variable
            firstCounter += 1 #whenever a character is added to the firstHolder, we record it to the firstCounter using the += 1
    for letter in secondUser: #iterate between the characters found in the secondUser variable
        if letter not in firstUser:
            '''
            conditional statement to check if the current character iterated is not found in the characters in the name of the first user
            > if the condition is true, then this statement will add the current character to the secondHolder variable then add 1 to the secondCounter
            variable. Adding one to the secondCounter variable whenever the character is not in the second name will help us determine the number
            of characters in the second user that are not found in the first user.
            > if the condition is false, then this statement will do nothing with the character
            '''            
            secondHolder += letter #if the current character iterated by the loop is not found in the name of the first user then add it to secondHolder variable
            secondCounter += 1 #whenever a character is added to the secondHolder variable, add 1 to the counter to determine the number of uncommon characters in the second user
    return firstCounter + secondCounter #return the total number of characters that are uncommon between the two users to the main program using return

def shuffler(count, list): #define a function named shuffler then add two input parameters
    #use this function to determine the appropriate 6K's relationship appropriate with the names of the two users.
    newCount = 0 #initialize newCount variable that will be used for indexing, set value to 0 to declare that it is an int variable
    while len(list) > 1: #create a loop that will only stop if the length of the list is already equal to or less than one
        if len(list) < count: #conditional statement to check whether the length of the list is less than the count parameter
            #if length of the list is less than count 
            if count % len(list) != 0: #check if the the remainder after dividing the count parameter by the length of the list is not equal to 0
                newCount = count % len(list) #if the remainder is not equal to 0 then update the value of the newCount variable
                #the value of the newCount variable will now be equal to the remainder of the count after dividing it by the length of the list
                del list[newCount - 1] #delete the element from the list using indexing
                list = list[newCount - 1:] + list[:newCount-1] #update the value of the list so that the length of the list will be reduced by one
                #the list will start from the succeeding element after an element was removed then will go back from the very first start 
                #use concatenation
            else: #if the remainder after dividing the count parameter by the length if the list is equal to 0 then this statement is true
                #if this statement is true:
                newCount = len(list) #update the value of the newCount equal to the value of the length of the list
                del list[newCount - 1] #remove the element at the index(newCount-1) in the list
                list = list[newCount - 1:] + list[:newCount-1] #update the value of the list so that the length of the list will be reduced by 1
                #the list will start from the succeeding element after an element was removed then will go back from the very first start 
                #use concatenation
        else: #if the length of the list is greater than the value of the parameter count then:
            del list[count - 1] #delete the element at index(count-1) from the list
            list = list[count - 1:] + list[:count - 1] #update the value of list so that its length will be reduced by 1
    #the loop will terminate once the length of the list is no longer greater than 1
    return list[0] #return the last remaining element of the list to the main program using return

def indexThenValue(element, list1, list2): #define a new function named indexThenValue then set three input parameters
    return list2[list1.index(element)] #return the element using the index value returned by the index(element) function at list1

relationshipValue = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6'] #create a list variable that will store the corresponding K values that will be used for the shuffle() function
absValue = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6') #create a tuple that will store the k values so that it is immutable
absStatus = ('Kaibigan', 'Kapuso', 'Kaaway', 'Kasal', 'Kilig (Crush)', 'Kapatid') #create a tuple that will store the corresponding K relationship status
#tuples are immutable so elements inside can only be called  or added but cannot be changed

# Let's create a brief introduction about the program using the print() function
print()
print('Welcome to the 6K\'s of Relationship Game! \nHave fun!')
print()

# Let's start asking for the users' names using the input() function
firstUser = input('Player 1 Name: ') #create an input variable that will store the name of the first user
secondUser = input('Player 2 Name: ') #create an input variable that will store the name of the second user

# Let's find out the total number of characters that the users' names do not have in common by calling the removeAndCound() function
notCommonCharacterNum = removeAndCount(firstUser, secondUser) #call the removeAndCount() function then set the parameters to the firstUser and secondUser
#order of paramaters is not important for this step

# Let's find out the value of the value of their relationship in the 6K's List by calling the shuffler() function
value6kRelationship = shuffler(notCommonCharacterNum, relationshipValue) #call the shuffler() function then set the parameters to notCommonCharacterNum and relationshipValue
#it's important to note that order for this function is important and absolute so programmer should not change it
#also note that for this function, the second parameter will only use lists that's why we are using the relationshipValue variable

# Let's find out their predicted relationship by calling the indexThenValue() function
predictedRelationship = indexThenValue(value6kRelationship, absValue, absStatus) #call the indexThenValue function then the parameters to value6kRelationship, absValue,  and absStatus
#note that order in the paramaters for this function is absolute and important so developers should interchange the parameters

# Let's prompt their relationship
print('Relationship Status :', predictedRelationship) #using the print() function, let's prompt the predicted relationship of the two users based on
#the element gathered from the indexThenValue() function

# Let's create a prompt to tell that the program is done
print()
print('Thank you for using the program!')
print()
