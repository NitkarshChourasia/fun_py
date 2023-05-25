"""
##Split a String Based on Vowels and Consonants

Write a function that takes a string, breaks it up and returns it with vowels first, consonants second.
For any character that's not a vowel (like special characters or spaces), treat them like consonants.


[Examples]

___
split("abcde") ➞ "aebcd"

split("Hello!") ➞ "eoHll!"

split("What's the time?") ➞ "aeieWht's th tm?"
_____



[Notes]

___
*) Vowels are a, e, i, o, u.
*) Define a separate is_vowel() function for easier to read code (recommendation).
___



[conditions] [control_flow] [functional_programming] [regex] 



-------------------------------------------------------------------
[Resources]
_________
Python String Methods
https://www.w3schools.com/python/python_ref_string.asp
Python has a set of built-in methods that you can use on strings.
_________
_________
sort() && sorted() Methods
https://docs.python.org/3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
_________
_________
How to check if a list is empty?
https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
For example, if passed the following: a = [] How do I check to see if a is empty?
_________
""" 
# Your code should go here:

def split(str1):
    vowels = list("aieouAEIOU")
    i = 0
    vowelLst1 = []
    consonantsLst1 = []
    while (i < str1.len()):
        if str1[i] in vowels:
            vowelLst1.append(str1[i])
        elif str1[i] != vowels:
            consonantsLst1.append(str1[i])
        i = i + 1
    outputCatStr = vowelLst1 + consonantsLst1  # Will it add the list?
    # WIll it work?
    outputCatStr = "".join(vowelLst1 + consonantsLst1)
    outputCatStr = "".join(outputCatStr)
    return outputCatStr


print(split("abcde")) # ➞ "aebcd"

print(split("Hello!")) # ➞ "eoHll!"

print(split("What's the time?")) # ➞ "aeieWht's th tm?"


# testing.
# checkResources.
# checkAgain.
