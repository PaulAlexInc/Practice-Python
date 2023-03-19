"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
"""
num=int(input("Enter the number to check : "))

def prime_check(number):
    is_prime = True
    for i in range(2, number):
        if number%i==0:
            is_prime = False
        
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
prime_check(number=num)