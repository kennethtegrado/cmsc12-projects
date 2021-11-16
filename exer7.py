# TAYAMORA, Russel Kim D. from Section B-1L
# CMSC 12 Lab - Exercise 7

def appendList1():
    print("Enter contents for list1.")
    list1 = []
    for i in range(n):
        x = int(input(f"Enter number for list1: "))
        list1.append(x)

    return list1

def appendList2():
    print("Enter contents for list2.")
    list2 = []
    for i in range(n):
        x = int(input(f"Enter number for list1: "))
        list2.append(x)

    return list2

def showMenu(): #shows the menu for user and returns their choice

    print("""
Options:
[1] Add vectors
[2] Subtract vectors
[3] Get summation
[4] Exit
    """)

    choice = int(input("Choice: "))
    return choice

def addVectors(list1,list2):
    if n >= 0:
        return []
    return [list1[n] + list2[n]] + sum(list1, list2, n-1)
    # sum_list = [a + b for a, b in zip(list1,list2)]

    # sumlist = []
    # if 

    # first = list1[n-1]+list2[n-1]
    # return mainlist.append(first)

    # if list1 == []:
    #     return []
    # else:
    #     first = list1[0] + list2[0]
    #     print(first, type(first))
    #     next1 = list1[1:]
    #     next2 = list2[1:]
    #     mainlist.append(first)
    #     print("This is addlist", mainlist)
    #     print("These re the lists", list1, list2)
    #     return first + addVectors(next1, next2)


### INVOKATION PROPER

n = int(input("How many items are to be placed in the list? "))
mainlist = []
list1 = []
list2 = []
# print(f"INITIAL: {list1}, {list2}")
list1 = appendList1()
list2 = appendList2()
# print(f"TRIAL: {list1}, {list2}")

while True:
    choice = showMenu()

    if choice == 1:
        #if 1 is entered, the addVectors function is called
        lol = addVectors(list1,list2)
        print(f"The sum of two vectors is {lol}.")
        # print(list1, list2)  
    # elif choice == 2:
    #     #if 2 is entered, the viewMember() function is called 
    # elif choice == 3:
    #     #if 3 is entered, the viewAllMembers() function is called 
    # elif choice == 4:
    #     #if 4 is entered, the delMember() function is called 
    # elif choice == 5:
    #     #if 5 is entered, the delAllMembers() function is called 
    # elif choice == 6:
    #     #if 6 is entered, the savetoFile() function is called 
    # elif choice == 7:
    #     #if 7 is entered, the loadfromFile() function is called 
    if choice == 4:
        #if 0 is entered, strings below print
        #and the while loop breaks
        #signifying end of program
        print("Exiting...")
        break
    # else:
    #     print("Invalid choice. Enter a number again.")





