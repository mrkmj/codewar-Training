'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
# returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
# returns 'Bart'

list([])
# returns ''
'''

#我的代码
def namelist(names):
    if names == ([]):
        return ''
    else:
        length = len(names)
        k = []
        for i in range(length):
            k.append(names[i]['name'])
        K_length = len(k)
        if K_length == 1:
            return k[0]
        else:
            st = ', '.join(k[:-1])+ ' & '+k[-1]
            return st
            
            
 #best solution，思路上是一样的，不过我多了要转成列表
 def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
