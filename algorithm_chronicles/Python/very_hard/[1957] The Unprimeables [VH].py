"""
####  The Unprimeables  ####

In this challenge, you have to establish if an integer is an Unprimeable number. To be Unprimeable, when a single digit of a composite number is exchanged with any digit from 0 up to 9, the new number obtained must not be a prime:
___
number = 14

Numbers obtained changing the first digit (1):

04 (4), 14, 24, 34, 44, 54, 64, 74, 84, 94
# Leading zeros are not considered

Numbers obtained changing the second digit (4):

10, 11, 12, 13, 14, 15, 16, 17, 18, 19

# Among the two series, 11, 13, 17 and 19 are primes
# 14 is not an unprimeable number

number = 200

Numbers obtained changing the first digit (2):

000 (0), 100, 200, 300, 400, 500, 600, 700, 800, 900
# Leading zeros are not considered

Numbers obtained changing the second digit (0):

200, 210, 220, 230, 240, 250, 260, 270, 280, 290

Numbers obtained changing the third digit (0):

200, 201, 202, 203, 204, 205, 206, 207, 208, 209

# Among the three series, there aren't primes
# 200 is an unprimeable number (the first of the series)
_____

Given a non-negative integer num, implement a function that returns:
___
*) The string "Prime Input" if num is prime.
*) The string "Unprimeable" if num is Unprimeable (accordingly to the above instructions).
*) If num is not Unprimeable, an array containing all the primes obtained after exchanging its digits, without duplicates and sorted ascendingly.
___



[Examples]

___
is_unprimeable(200) ➞ "Unprimeable"

is_unprimeable(14) ➞ [11, 13, 17, 19]

is_unprimeable(2) ➞ "Prime Input"
_____



[Notes]

___
*) When changing the first digit, leading zeros are not considered part of the new number obtained.
*) Despite is still an unproofed theory, as far as we know every even number (except 2) is not prime. You are free to choose to use this discriminant when you check the number obtained after the change of a digit.
*) The same concept can be applied also to primes. Primes that do not return other primes when their single digits are changed (apart from the number itself) are called Weakly Primes: the first prime of this series is 294001.
___



[conditions] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Unprimeable Numbers
http://www.numbersaplenty.com/set/unprimeable_number/
A composite number "n" is called unprimeable if it cannot be turned into a prime by changing a single digit. For example, 144 is not unprimeable, because changing the l …
_________
_________
How to Check If a Number Is Prime
https://en.wikipedia.org/wiki/Primality_test
A primality test is an algorithm for determining whether an input number is prime. Among other fields of mathematics, it is used for cryptography. Unlike integer factor …
_________
_________
Replace Character at Specific Position
https://pythonexamples.org/python-string-replace-character-at-specific-position/
To replace a character with a given character at a specified index, you can use python string slicing as shown below: string = string[:position] + character + string[p …
_________

"""
#Your code should go here:

