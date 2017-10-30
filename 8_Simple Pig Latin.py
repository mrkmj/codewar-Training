'''
Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay

Ps:Only letters!!!!!!!!!
'''

#My bad code
def pig_it(text):
    ls = text.split()
    lengyh = len(ls)
    result = []
    for i in ls:
        each = list(i)
        if i.isalpha():
            each = each[1:] + each[:1] + ['a'] + ['y']
            each = ''.join(each)
            result.append(each)
        else:
            result.append(''.join(each))
    return ' '.join(result)
    
#Better code
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
    
    
#str.split() 参数默认是空格
