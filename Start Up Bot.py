'''
start_program()

initialize list variable named months to contain the  months of the year: [
    empty string placeholder, #for indexing
    January,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December,
];

initialize list variable named daysMonths to contain the number of days per month: [
    1, #first day of January
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
];

initialize list variable named days: [
    empty string placeholder, #use for indexing
    Friday, #start with friday since january 1, 2021 is friday
    Saturday,
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday, #end with thursday since that's the 7th day
]

initialize input variable named month to ask for a number of the month from the user;

if month is a number from 1-12 then:
    initialize variable named totalDays to store the number of days and set temporary value to 0;

    for every number of days per month in daysMonths starting from first month to month written by user, iterate:
        add current value of days per month from list daysMonths to totalDays
    end for loop;

    if value of totalDays is greater than seven then:
        if there are no remainder after dividing totalDays with 7 then:
            initialize integer variable named dayWeek and set value to 7;
        else:
            initialize integer variable named dayWeek and set value to the
            remainder of totalDays after dividing it by seven;
    else then: #totaldays is less than seven
        initialize variable named dayWeek and set value to equal to totalDays

    initialize variable named weekDay and set the value to equal to the value of list days at index dayWeek;

    initialize variable named chosenMonth and set the value to equal to the value of list months at index month;

    print a prompt that says that the first day of the value of chosenMonth is the value of weekDay;
else:
    print a prompt that says invalid input;

end_program()
'''

month = int(input('Enter Month: '))

months = ['Empty','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
daysOfMonths = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Empty','Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday'] #every 7 days 
# days2 = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

totalDays = 0
for i in daysOfMonths[0:month]:
    totalDays += i 

if totalDays > 7:
    if totalDays % 7 == 0:
        dayWeek = 7
    else:
        dayWeek = totalDays % 7
else:
    dayWeek = totalDays
print(totalDays)
print(dayWeek)
print(months[month])
print(days[dayWeek])

'''
Friday - 1
Monday - 2
Monday - 3
Thursday - 4
Saturday - 5
Tuesday - 6
Thursday - 7
Sunday - 8
Wednesday - 9
Friday - 10
Monday - 11
Wednesday - 12
'''

_iL0veCMsc12 = 'hahaha'
x = float(5.4)

