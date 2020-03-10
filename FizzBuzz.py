#! python3

# This program prints numbers from 1-100, replacing multiples of 3 with Fizz, multiples of 5 with Buzz and multiples of both with FizzBuzz

for fizzBuzz in range(1,101): # For all numbers in range 1-101 (not including 101) assign a number to variable: fizzBuzz

    if fizzBuzz % 15 == 0: 
        print('FizzBuzz') # Use a modulus operation to find the remainder of the number when divided by 15. If the remainder = 0 (therefore a perfect division), then print FizzBuzz 
                                           # This needs to be first so that it ensures FizzBuzz is printed as it also fits the criteria of the other two and would be skipped otherwise
    elif fizzBuzz % 3 == 0:
        print('Fizz') # Elseif statement for the modulo operator of 3. If the statement above is false, then proceed to this. Print Fizz

    elif fizzBuzz % 5 == 0:
        print('Buzz') # Same thing but with 5 instead. Print Buzz
      
    else:
        print(fizzBuzz) # If all the statements are false, it just prints the number
