'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

uniqueInOrder('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
uniqueInOrder('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
uniqueInOrder([1,2,2,3,3])       == [1,2,3]
'''

#My code
def unique_in_order(iterable):
    t = list(iterable)
    length = len(t)
    for i in range(length-1):
        while t[i] == t[i+1]:
            t.pop(i+1)
            t.insert(0,0)
    c = t.count(0)
    t = t[c:]
    return t
    
#Clever code
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
    
#所以itertools这个是什么....
