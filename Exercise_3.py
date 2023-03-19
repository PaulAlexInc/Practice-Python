"""
Take a list, say for example this one:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1.Instead of printing the elements one by one, make a new list that has all the elements 
less than 5 from this list in it and print out this new list.
2.Write this in one line of Python.
3.Ask the user for a number and return a list that contains only elements from the original 
list a that are smaller than that number given by the user.

https://www.practicepython.org/solution/2014/02/26/03-list-less-than-ten-solutions.html
"""

n=int(input("Enter a number :")) #Extras:3
print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i<5 if i<n]) # creating a new list, and printing all the elements less than 5 in the original list, in a single line using list complrehension
print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i<n])#Extras:3

#Ref: https://stackoverflow.com/questions/32580489/python-for-and-if-on-one-line