'''
Problem 4
15/15 points (graded)
Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.

assume L is not empty
assume 0 < n <= len(L)
This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]

Your function does not have to be recursive. Do not leave any debugging print statements when you paste your code in the box.
'''
def getSublists(L, n):
    l = []
    x = 0
    while n <= len(L):
        l += [L[x:n]]
        x, n = x+1, n+1
    return l

print( getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4))
