'''
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 

spinWords( "This is a test") => returns "This is a test" 

spinWords( "This is another test" )=> returns "This is rehtona test"

'''
#我的代码
def spin_words(sentence):
    words = sentence.split(' ')
    num = len(words)
    for each in range(num):
        length = len(str(words[each]))
        if length >= 5:
            s = str(words[each])
            words[each] = s[::-1]
    st = ' '.join(words)
    return st
    
#其实思路一样，简化
def spin_words(sentence):
   
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
