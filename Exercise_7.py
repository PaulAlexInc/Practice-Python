"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even 
elements of this list in it.

https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
"""

print([i for i in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] if i%2==0])

"""
alternate solutions : https://www.practicepython.org/solution/2014/03/26/07-list-comprehensions-solutions.html
"""