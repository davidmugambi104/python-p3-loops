#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
        print("Happy New Year!")
        
       
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)  # Convert the number to a string for consistency with JavaScript's behavior

def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))

# Calling the function to print the FizzBuzz sequence


    

def fizzbuzz():
    # code goes here!
    pass
