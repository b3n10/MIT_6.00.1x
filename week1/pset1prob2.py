"""
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
# Paste your code into this box

count, occur = 0, 0

for x in range(len(s)):
    if count+2 <= len(s) - 1:
        if s[count] == 'b' and s[count+1] == 'o' and s[count+2] == 'b':
            occur += 1
        count += 1

print("Number of times 'bob' occurs is: " + str(occur))
