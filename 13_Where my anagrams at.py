'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''


#My code(so bad...)
def anagrams(word, words):
    target = list(word)
    t_length = len(target)
    b = []
    for j in range(len(words)):
        middle = list(words[j])
        a = []
        if len(middle) == t_length:
            for i in range(t_length):
                if target.count(target[i]) == middle.count(target[i]):
                    a.append(middle[i])
                else:
                    a = []
                    break
            c = ''.join(a)
            if c != '':
                b.append(c)
    return (b)
    
    #Better
    def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
