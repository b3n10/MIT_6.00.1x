'''
Exercise: apply to each 1
5/5 points (graded)

ESTIMATED TIME TO COMPLETE: 2 minutes

Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
Assume that

testList = [1, -4, 8, -9]
For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

Example Question:

print(testList)
[5, -20, 40, -45]
'''
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]

def div5(i):
    i = i + 1
    return i

applyToEach(testList, div5)
print(testList)
