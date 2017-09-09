"""
Problem 3
15.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""
def abc(s):
    word, collection = "", ""
            
    #c is current index
    for c in range(len(s)):
        #search if not last char
        if not c+1 == len(s):
            if s[c] <= s[c+1]:
                word += s[c]
            else:
                word += s[c]
                collection = collection if len(collection) >= len(word) else word # ternary operator to get longest substring
                word = "" # clear word before next substring
        #if last char, add to collection and stop
        else:
            word += s[c]
            return collection if len(collection) >= len(word) else word
    return collection

print("Longest substring in alphabetical order is: " + abc(s) )
