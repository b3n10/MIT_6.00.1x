'''
Exercise: how many
5/5 points (graded)
ESTIMATED TIME TO COMPLETE: 6 minutes

Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

print(how_many(animals))
6
'''
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum_of_val = 0
    
    for d in aDict.values():
        for v in d:
            sum_of_val += 1
    
    return sum_of_val

print( how_many({'u': [10, 15, 5, 2, 6], 'B': [15]}) )
