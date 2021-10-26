'''
Exercise 5: Dictionaries

CMSC 12 | Course

Submitted to:
Professor Aragones

Submitted by:
TEGRADO, Kenneth Renz A.
'''

'''
The purpose of the program is to create an application that can hold records of fitness club members.

Our application should be able to do the following:
> Add a member record
> View a member record initially placed in the program
> View all member records of all recorded members in the program
> Edit a member record wherein updating weight will update BMI & Type and height should not be editable
> Delete a member record using a member id as the key
> Delete all member records will delete all data of the program
> Exit to close the program
'''

# All functions used by the program


def menu():  # define a function named menu but there's no need to set an input parameter
    # use this function to show the menu that will prompt all the functions of the program
    # this function will also allow user to choose a function that they want to utilize from the program
    print("Options:\n [1]Add a member\n [2]View a member record\n [3]View all members\n [4]Edit member record\n [5]Delete a member record\n [6]Delete all member records\n [0]Exit ")
    # use print() function to show all the options available for the program
    # ask for user input using input() function
    choice = input("Enter your choice: ")
    # store the user's choice of function in the choice variable
    return choice  # return the value of the choice variable to the main program


def idGenerator(dict):  # define a function named idGenerator and set one input paramater to a dict
    # use this function to generate an id for a user
    # use the dict parameter to check a dictionary
    # check if the dict contains an item using the len() function
    # the number of items inside the dict parameter indicates the number of members inside the database
    members = len(dict)
    if members == 0:  # condition to check if there aren't any member inside the database
        # if there are no members inside the database then do the this
        id = 'M001'  # create a variable id then set the value to the string M0001
    else:  # if the database has any members then do this condition
        # create a lastElement variable that will store the key of the last item inside the dict parameter
        # store all the keys of the dict parameter in a list using the last() function
        # then use indexing to make the last key be stored inside the lastElement variable
        lastElement = list(dict.keys())[-1]
        idNum = ''  # create an empty string variable named idNum that will store the number key of the last member placed on the database
        for char in lastElement:  # iterate every character of the lastElement variable
            if char.isnumeric():  # condition to check if a character iterated is a numeric character
                idNum += char  # concatenate the character to the idNum variable

        # create newIdNumber variable that will be used to store the new id number allocated for the new member inside the database
        # add one to the value of the idNumber to so that it will indicate that there's a new number succeeding the previous id number
        # use the int() function to convert a string to an integer
        newIdNumber = int(idNum) + 1
        if 1000 > newIdNumber >= 100:  # condition to check if the new id number is greater than or equal to 100 or less than 1000
            # set the value of id to this string format
            id = "M" + str(newIdNumber)
        elif 100 > newIdNumber >= 10:  # condtion to check if the new id number is greater than or equal to 10 but less than 100
            # set the value of id to this string format if this condition is met
            id = "M0" + str(newIdNumber)
        elif 10 > newIdNumber > 0:  # condition to check if the new id number is greater than 0 but less than 10
            # set the value of the id variable to this string format if this condition is met
            id = "M00" + str(newIdNumber)
    return id  # return the value of the id variable back to the main program using the return method


def bmi(weight, height):  # define a user function named BMI and set two input parameters
    # use this function to compute for the BMI of the person
    # note that the parameters for this function must follow the proper order
    # using the formula for BMI compute for the BMI of the user
    bmi = round(weight / ((height/100) ** 2), 1)
    # use the round() function and set the decimal place to 1 since we can only accept a number with one decimal place
    # store the value of the computed BMI on the bmi variable
    if 0 < bmi < 18.5:  # condition to check whether the bmi of the person is less than 18.5 but greater than 0
        # if the condition stated above is true then do this
        index = "Underweight"  # set the index to the string Underweight
        # a bmi of less than 18.5 is considered underweight
    elif 18.5 <= bmi <= 24.9:  # another condition to check if the bmi of the person is greater than or equal to 18.5 but less than or equal to 24.9
        # if the condition above is true then do this
        index = "Normal"  # set the value of the index variable to Healthy
        # base on the BMI index, a bmi between 18.5 and 24.9 is a healthy bmi
    elif 25 <= bmi <= 29.9:  # another condition to check if the bmi of the person is greater than or equal to 25 but less than or equal to 29.9
        # if the condition is true then do this
        index = "Overweight"  # set the value of the index to the string Overweight
        # base on the BMI index, a bmi between 25 and 29.9 is overweight
    elif bmi >= 30:  # another condition to check if the bmi of the person is greater than or equal to 30
        # if the condition is true then do this
        index = "Obese"  # set the value of the index variable to the string Obese
        # base on the BMI index, a bmi greater than 30 is considered obese
    else:  # if the bmi variable did not meet any of the conditions set above use this condition
        # set the value of the index variable to the string Cannot be determined
        index = "Cannot be determined"
        # this is an indicator that the input of the user is not valid
    # using the return method, send the value of the bmi and index to the main program
    return bmi, index  # this will return a tuple data type since we will send two variables
    # we are going to need to unparse the data if we are going to utilize the elements one by one
    # note that using a tuple data type will help us create an immutable data structure


def addMem(id, dict):  # define a user function named addMem and set the two parameters to id and dict
    # use this function to add a member to a dictionary data structure
    # the id parameter will be used as the key for the values
    # ask for the user's name using the input() function then store the value in the name variable
    name = input("Enter name: ")
    # ask for the user's weight using the input() function then use the float() function to ensure that the variable placed will be converted to a float object
    weight = float(input("Enter weight (kg): "))
    # ask for the user's height using the input() function then use the float() function to ensure that the variable placed will be converted to a float object
    height = float(input("Enter height (cm): "))
    # determine what is the bmi of the user and their classification by using the bmi() user function then set the parameters to the weight and height variables respectively
    bmiInfo = bmi(weight, height)
    # using the f method tell the user what is their BMI and classification by unparsing the data from the bmiInfo variable
    print(f'BMI is {bmiInfo[0]}\nType is {bmiInfo[1]}')
    # create an element in the dict parameter
    # set the key to the value of the ID parameter then the value to the list containing the name, weight, height, and bmiInfo variables respectively
    # order of the variables to placed on the values must be followed strictly with the same format below
    dict[id] = [name, weight, height, bmiInfo]
    return dict  # return the new dict parameter to the main program using the return method


def viewMem(dict):  # define a new user funciton named viewMem then set the input parameter to dict
    # use this function to view a member data
    record = ''  # create an empty string that will use the elements inside the dict parameter and transform it to a variable that can be easily understood
    # ask the user what is the id of the member that he is going to check using the input() function
    id = input("Enter member ID: ")
    if id in dict:  # condition to check if the id placed by the user is inside the dict parameter
        # if the is in their then
        # unparse the data of the element at the dict with the key id
        # strictly follow the format of unparsing the values using the variables below because that is the order of the data inside the dict parameter
        name, weight, height, bmiInfo = dict[id]
        # concatenate this string to the value of the record
        record += "=== Member Information ===\n"
        # using the f function set the the formatting to the provided string
        record += f'({id}) - {name} {weight} kg {height} cm (BMI: {bmiInfo[0]}; {bmiInfo[1]})\n'
    else:  # if the id is not in the dict parameter then
        # concatenate this string to the record variable
        record += 'Sorry, the record does not exist!\n'
    return record  # using the return method, give the value of the record variable back to the main program


def viewAll(dict):  # define a new user function named viewAll and set the parameter to dict
    # create a string variable named record then set the initial value to this string
    record = '=== List of members ===\n'
    if len(dict) > 0:  # use this condition to check if the dict parameter is not empty
        for id, data in dict.items():  # iterate at every items inside the dict parameter
            # at every iteration
            # unparse the data variable which is the values inside an item currently iterated
            name, weight, height, bmiInfo = data
            # using the f function, concatenate this string to the record variable
            record += f'({id}) - {name} {weight} kg {height} cm (BMI: {bmiInfo[0]}; {bmiInfo[1]})\n'
    else:  # if the dict paramater is empty then do this condition
        # concatenate a string that says the record is empty to the record variable
        record += 'Sorry, record is empty!'
    return record  # using the return method, give the value of the record variable back to the main program


def editMem(dict):  # define a new user function named editMem and set the parameter to dict
    # use this function to edit the weight of a user which will also change their BMI after use
    # ask the user for the id of the member that they are going to edit using the input() function
    id = input("Enter the ID of user that you wish to edit: ")
    if id in dict:  # condition to check if the user id is in the dict parameter
        # ask the user for the new weight using the input() function then utilize the float() function to tell the program that the object is a float object
        weight = float(input("Enter your new weight here (kg): "))
        # update the new weight of the user by changing its value to the latest weight placed
        dict[id][1] = weight
        # compute for the new bmi and its classification by calling the bmi() function and set the parameters with the variables below
        newBMI = bmi(weight, dict[id][2])
        # update the value of the BMI placed on the dict parameter using this method
        dict[id][3] = newBMI
        # print a prompt that says that the editing process is a success
        print("Successfully Edited!")
        return dict  # return the new value of the dict back to the main program using the return method
    else:  # if the id placed by the user is not in the dict parameter
        # print a prompt that says that the id is not in the database
        print("Member does not exist!")


def delMem(dict):  # define a new user function named delMem then set the input parameter to dict
    # use this function to delete a member from the database
    # ask for the id from the user using the input() method
    id = input("Enter member ID: ")
    if id in dict:  # condition to check if the id placed by the user is in the database
        # use the del method to delete an item from the dict parameter given the id as the key
        del dict[id]
        # print a prompt that says that the deleting process is a success
        print(f'Member {id} successfully deleted.')
        return dict  # return the updated dict parameter back to the main program using the return method
    else:  # if the id is not in the database then follow this condition
        # print a prompt that says that the the user is not in the database
        print('Sorry, the user is not in the database!')


def delAll(dict):  # define a new function named delAll then set the parameter to dict
    # return the updated value of the dict parameter back to the main program
    # use the clear() function to delete all items inside the dict parameter
    return dict.clear()


# Start of Main Program

# create an empty dictionary variable then set the name to memberData
# use the camel case in naming since it is more conventional
# use this dictionary to act as the database of the program
memberData = {}

# print a prompt that informs the user that the program is now starting
print("Welcome to Aubrey Simp's Fitness Club")

while True:  # create an infinite loop that will continuously ask the user for a function until the loop is terminated
    choice = menu()  # call the menu() function to prompt all available functions of the program
    # store the returned value to the choice variable
    if choice == "1":  # condition to check if the user placed 1 as their choicce
        # call the addMem function to add a user to the program
        # set the parameters to the value generated by the idGenerator() function and the dictionary memberData
        addMem(idGenerator(memberData), memberData)
        # print a prompt that says that a member is successfully added to the database
        print("Successfully Added!")
        print()  # use a blank print() function to create an empty line in the program
    elif choice == "2":  # if the user chose 2 on the otherhand
        # call the viewMem() function to view a member from the database
        # print the returned value of the viewMem() function
        print(viewMem(memberData))
    elif choice == "3":  # if the user chose 3 as their choice
        # call the viewAll() function to show all data placed on the database
        # print the returned value of the viewAll() function
        print(viewAll(memberData))
    elif choice == "4":  # if the user chose 4 as their choice
        # call the editMem() user function then set the parameter to the dictionary memberData
        editMem(memberData)
    elif choice == "5":  # if the user chose 5 as their choice
        # call the delMem() user function and set the parameter to the dictionary memberData to delete an item inside it
        delMem(memberData)
    elif choice == "6":  # if the user chose 5 as their choice
        # call the delAll() user function to delete all the items inside the dictionary memberData
        delAll(memberData)
    elif choice == "0":  # if the user chose 0 for their choice
        # print a prompt that thanks the user for using the program
        print("Thank you for using the program!")
        break  # break the loop
    else:  # if the user gave a choice not in the function specified the program then use this condition
        # print a prompt that says that it is an invalid choice
        print("Invalid choice!")

# End of the program
