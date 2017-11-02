'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0..255 (included).

Input to the function is guaranteed to be a single string.

Examples

// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note: leading zeros (e.g. 01.02.03.04) are considered not valid in this kata!
'''

#My code
def is_valid_IP(strng):
    test = strng.split('.')
    count = 0
    if len(test) == 4 and (''.join(test)).isdigit():
        for i in range(4):
            middle = list(test[i])
            print(middle)
            if int(middle[0]) == 0:
                break
            else:
                if int(test[i])<256 and int(test[i])>0:
                    print(test[i])
                    count += 1
                else:
                    break
    if count == 4:
        return True
    else:
        return False
        
    #Better 
    def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4
