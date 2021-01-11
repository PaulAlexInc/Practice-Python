"""Given a number n. The problem is to efficiently check whether n is a 
multiple of 4 or not without using arithmetic operators.

https://www.geeksforgeeks.org/efficiently-check-whether-n-multiple-4-not/

https://www.youtube.com/watch?v=ke-Mai2m6Cg&feature=emb_logo"""

#Bitwise alogorithms

"""To check if any number n is a multiple of b, we can use the modulo operator
but if b is a power of 2 then we can efficiently do it using bitwise operation.
if (n&(b-1)) is 0 then, n is a multiple of b

Time complexity is O(1)
Space complexity is O(1)

if n=24 and b=4
b is a power of 2
logic : if (n&(b-1))==0
"""
num = int(input("Enter a number :"))
if(num & 3==0): #b=4 here so b-1==3
    print("Yes")
else:
    print("No") 