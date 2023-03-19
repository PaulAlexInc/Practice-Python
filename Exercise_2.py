'''
Ask the user for a number. Depending on whether the number is even or odd, print out an 
appropriate message to the user. Hint: how does an even / odd number react differently 
when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide 
by (check). If check divides evenly into num, tell that to the user. If not, print a different 
appropriate message.

https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
'''

num = int(input("Enter a number :"))
if num%4==0:
    print("The number is a multiple of 4")
elif num%2==0:
    print("Even number")
else:
    print("Odd number")
num = int(input("Enter a number to divide(dividend) :"))
check = int(input("Enter a number to divide the number you entered by(divisor) :"))
print(f"{check} divides evenly into {num}" if num%check==0 else f"{check} does not divide evenly into {num}" )

"note : Evenly divisible means that you have no remainder.20 is evenly divisible by 5 since 20 / 5 = 4"