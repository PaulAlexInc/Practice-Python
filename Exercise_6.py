
"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)

https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

"""
string = input("Enter a string :")
s = string[::-1]
print (s)
print("true" if s==string else "false")
