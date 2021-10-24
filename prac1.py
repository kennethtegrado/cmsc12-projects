countries = {
    
}

x = ''

while True:
    print("Options:\n [1] Display the capital city given the country name\n [2] Add a country record\n [3] View all countries\n [0] Exit")
    choice = input("Choice: ")
    if choice == '1':
        countryName = input('Country name: ')
        if countryName in countries:
            print('The capital city of', countryName, 'is', countries[countryName], '\n')
        else:
            print('There are no records of the country', countryName, '\n')
    elif choice == '2':
        countryName = input('Country name: ')
        countryCapital = input('Capital city: ')
        countries[countryName] = countryCapital
        print('Successfully added', countryName, '\n')
    elif choice == '3':
        print(countries, '\n')
    elif choice == '0':
        print('Thank you for using the program')
        break
    else:
        print('Invalid input. \n Try again.\n')