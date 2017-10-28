#判断一个数是否为平方数
#http://www.codewars.com/kata/youre-a-square/python
'''
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples

is_square (-1) # => false
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false

'''

#我的方法
#1050ms
def is_square1(n):
  i = 1
  if n < 0:
    return False
  else:
    while n!=0 and n>0:
      n -= i
      i+=2
    if n == 0:
      return True
    else:
      return False
      
#别人的高支持方法
#203ms
from math import sqrt

def is_square2(n):
    return n > 0 and sqrt(n).is_integer()
