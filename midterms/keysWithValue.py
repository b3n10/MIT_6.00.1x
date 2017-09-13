'''
Problem 5
20/20 points (graded)
Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.
'''
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    l = []
    for i in aDict:
        if target == aDict[i]:
            l.append(i)
        elif not target in aDict.values():
            return l
    return sorted(l)

print(keysWithValue({1: 2, 2: 1, 3: 1, 4: 2, 5: 3, 7: 3, 8: 4, 9: 1, 10: 0}, 4))
