'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are 
common between the lists (without duplicates). Make sure your program works on two 
lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this 
point - we’ll get to it soon)

https://www.practicepython.org/solution/2014/03/19/05-list-overlap-solutions.html
'''


'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''
import random
randomlist1=[]
randomlist2=[]
for i in range(0,5):
    randomlist1.append(random.randint(1,30))
    randomlist2.append(random.randint(1,30))

print(randomlist1)
print(randomlist2)
print(list(set([i for i in randomlist1 if i in randomlist2])))