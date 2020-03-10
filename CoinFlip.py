#! python3
# This program shows the outcome of an amount of counflips chosen by the user

import random

coinFlip = input('How many times do you want to flip the coin? ')

heads = 0
tails = 0

try:
    if int(coinFlip) < 0:
        print('\nYou attempt to flip the coin and it vanishes into thin air. It doesn\'t like negative numbers.')

    for i in range(1, (int(coinFlip) + 1)):
        if random.randint(0, 1) == 1:
            heads = heads + 1
        else:
            tails = tails + 1
            
    print('\nFlipping a coin ' + str(coinFlip) + ' times.')
    print('Heads came up ' + str(heads) + ' times and tails came up ' + str(tails) + ' times.')

except ValueError:
    print('\nPlease enter a valid integer!')
    

