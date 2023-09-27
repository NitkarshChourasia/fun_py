"""
####  Columnar Cipher  ####

The columnar cipher is a transposition cipher that works like this.
Start with a secret message:
___
msg = "Meet me by the lake at midnight. Bring shovel."
_____

Transform uppercase letters into lowercase and remove punctuation and spaces:
___
msg = "meetmebythelakeatmidnightbringshovel"
_____

Then, pick a keyword made out of distinct letters:
___
keyword = "python"
_____

Break up the message into chunks of the same length as the keyword, and write them in rows under the keyword. Then, number the columns based on the alphabetised order of the letters in the keyword:

Read off the enciphered message (ciphertext) from the columns, in the order specified by the numbers:
___
ciphertext = "thaiivelmhglmetgnembaitsetenroeykdbh"
_____

If the message length is not a multiple of the keyword length, fill in each blank space with "x". For example:
___
msg = "Meet me at midnight."

keyword = "python"
_____


Create a function that takes a string and a keyword. Return the ciphertext if the string is in plaintext (i.e. broken up into normal English words and punctuated), or the deciphered message if the string is in ciphertext. The resulting deciphered message will not have spaces.


[Examples]

___
c_cipher("Meet me by the lake at midnight. Bring shovel.", "python")
➞ "thaiivelmhglmetgnembaitsetenroeykdbh"

c_cipher("meeanbsleyamgioxebltirhxttkihnvxmhedtgex", "monty")
➞ "meetmebythelakeatmidnightbringshovelxxxx"

c_cipher("Mission Delta Kilo Sierra has been compromised. Kill Steve. Evacuate", "cake")
➞ "ioliiabcrsiteuxmieksrsnpiksecesdaoraemmdlvatxsntleheooelevax"
_____



[Notes]

N/A


[arrays] [cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Floor Division
https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html
Also referred to as integer division. The resultant value is a whole integer, though the result’s type is not necessarily int.
_________
_________
RegEx in Python (Part 1)
https://realpython.com/regex-python/
In previous tutorials in this series, you've seen several different ways to compare string values with direct character-by-character comparison. In this tutorial, you'l …
_________
_________
String islower() Method
https://www.programiz.com/python-programming/methods/string/islower
Returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
_________
_________
Columnar Transposition Cipher
https://www.geeksforgeeks.org/columnar-transposition-cipher/
The Columnar Transposition Cipher is a form of transposition cipher just like Rail Fence Cipher. Columnar Transposition involves writing the plaintext out in rows, and …
_________

"""
#Your code should go here:

