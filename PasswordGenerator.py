#! python 3

# This program generates a random password with a length based on human input (random module is not cryptographically secure)

import random

try:
    
    characters = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWKYZ123456789~!@#$%^&*_-+=`|\\(){}[]:;\'<>,.?/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWKYZ123456789~!@#$%^&*_-+=`|\\(){}[]:;\'<>,.?/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWKYZ123456789~!@#$%^&*_-+=`|\\(){}[]:;\'<>,.?/'''

    passLength = int(input('How long would you like your password? (Max 276) '))

    password = ''.join(random.sample(str(characters), passLength))

    print('Your random password is: ' + str(password))

except ValueError:
    
    print('Please enter a valid integer or make sure it isn\'t over 276.')
