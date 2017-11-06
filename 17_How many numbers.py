'''
We want to generate all the numbers of three digits that:

the value of adding their corresponding ones(digits) is equal to 10.
their digits are in increasing order (the numbers may have two or more equal contiguous digits)
The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334

Make a function that receives two arguments:

the sum of digits value
the amount of desired digits for the numbers
The function should output an array with three values:
[1,2,3]

1 - the total amount of all these possible numbers

2 - the minimum number

3 - the maximum numberwith

The example given above should be:

find_all(10, 3) == [8, 118, 334]
findAll(10, 3) ---> [8, "118", "334"]
If we have only one possible number as a solution, it should output a result like the one below:

find_all(27, 3) == [1, 999, 999]
findAll(27, 3) ---> [1, "999", "999"]
If there are no possible numbers, the function should output the empty array.

find_all(84, 4) == []
findAll(84, 4) ---> []
The number of solutions climbs up when the number of digits increases.

find_all(35, 6) == [123, 116999, 566666]
findAll(35, 6) ---> [123, '116999', '566666']
Features of the random tests:

Numbers of tests: 111
Sum of digits value between 20 and 65
Amount of digits between 2 and 15
'''

#My code(no mine in fact)
def find_all(sum_dig, digits):
    if sum_dig > digits * 9:
        return []

    if sum_dig == digits*9:
        return [1, int('9' * 3), int('9' * 3)]

    num = [1] * digits
    print(num)
    res = []

    while num[0] != 10:
        if sum(num) == sum_dig:
            res.append(int(''.join(map(str, num))))

        for i in range(digits - 1, -1, -1):
            num[i] += 1
            if num[i] != 10:
                break
                
        for i in range(1, digits):
            if num[i] == 10:
                num = num[:i] + [num[i - 1]] * (digits - i)
                break
    return [len(res), res[0], res[-1]]
    
    
