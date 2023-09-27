"""
####  Collatz Calculator  ####

A Collatz sequence is generated by repeatedly applying the following rules to an integer and then to each resulting integer in turn:
___
*) If even: divide by 2.
*) If odd: multiply by 3, then add 1.
___

The Collatz conjecture states that, for any initial positive integer, you will eventually reach the number 1.
Write a function that, for an initial positive integer n, returns a list containing 2 values:



[Examples]

___
collatz(17) ➞ [12, 52]
# Because 17 – 52 – 26 – 13 – 40 – 20 – 10 – 5 – 16 – 8 – 4 – 2 – 1
# takes 12 steps and 52 is the highest number reached.

collatz(6) ➞ [8, 16]

collatz(21) ➞ [7, 64]
_____



[Notes]

N/A


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
The Collatz Sequence
https://codereview.stackexchange.com/questions/229270/python-the-collatz-sequence
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd …
_________

"""
#Your code should go here:

