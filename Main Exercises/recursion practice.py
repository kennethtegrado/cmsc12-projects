# Recursion Division Practice

def division(x, y):  # define a new user function named Division and set two parameters x and y
    # x represents the dividend
    # y represents the divisor
    # base case
    if y > x:  # condition to check if divisor is now greater than dividend
        return 0  # return 0 if divisor is now greater than dividend
    # 1 will be our counter of the instances that the recursion is possible
    # everytime the recursion is possible then add 1 to represent that we divided the number
    return 1 + division(x - y, y)


print(division(9, 3))
