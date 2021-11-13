'''
Solution for Adding Two Matrices by Wizby

Our goal in this challenge is to create a program that can help us generate a new list that contains the sequence of all the sum of the elements of two lists

Notes:
> We can only accept two lists
> The lists provided is not from the user but from the main program itself
> The lengths of the lists must be EXACTLY the same
> List and Arrays are the SAME

Options:
    We can use two solutions for the program
    1. List Comprehension
'''


# All functions used by the program
def sumMatrix(l1, l2):  # define user function sumMatrix
    # set the parameters to l1 and l2 both indicating list 1 and list 2
    # use this function to create a sum of a list of each elements from list 1 and list 2
    return [[l1[i][j] + l2[i][j] for j in range(len(l1[i]))] for i in range(len(l1))]
    # use the return method to return the new list created from the list comprehension above


def main(l1, l2):  # define user function main
    # use this function to call the program
    print('\nThis is the result of our code:\n', sumMatrix(l1, l2), '\n')


# Start of the program
# init variable list1 with this value
list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# init variable list2 with this value
list2 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]

# call the main() function then set the arguments to list1 and list2
main(list1, list2)

# End of the Program
