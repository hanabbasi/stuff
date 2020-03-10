#! python3
# This program outputs numbers with their corresponding square values according to user input

userValue = input('Produce squared values up to: ')

try:
    for i in range(1,(int(userValue) + 1)):
    
    #if (i**2) <= 200:           # Limit code to a squared value of less than 200
        print(i, end = '  '),
        print(i**2)

except ValueError:
    print('\nPlease enter a valid integer!')
