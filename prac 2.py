
n = int(input('Enter a new number: '))

for i in range(1, n+1):
    if (i ** (1/2)) % 1 == 0:
        print(i , 'number is a perfect square!')
    if (i ** (1/3)) % 1 == 0 or (i ** (1/3)) % 1 > 0.9999:
        print(i, 'number is a perfect cube!')

'''

start_program()

initialize input variable named N to ask for a number from the user;

for every number from 1 to N, iterate:
    if the current number is a perfect square:
        print prompt that shows the value of the current number and says it's a perfect square;
    else:
        the program will do nothing;
    
    if the current number is also or just a perfect cube:
        print prompt that shows the value of the current number and says it's a perfect cube;
    else:
        the program will do nothing;
end for loop;

end_program()

    
'''