"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. (Hint: order of 
operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)

https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""

name = input("Enter your name :")
age = int(input("Enter your age :"))
print(f"{name} will turn 100 years old in {2021 + (100-age)}")
copies = int(input("Enter the number of copies of the previous message you need :"))
for i in range(0,copies):
    print(f"{name} will turn 100 years old in {2021 + (100-age)}")