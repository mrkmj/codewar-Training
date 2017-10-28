#找出最大最小值，坑爹的题目
#主要是我忘记了split的方法，硬解题目麻烦
'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

Kata.HighAndLow("1 2 3 4 5"); // return "5 1"
Kata.HighAndLow("1 2 -3 4 5"); // return "5 -3"
Kata.HighAndLow("1 9 3 4 -5"); // return "9 -5"

典型这样子输出。。。
high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
high_and_low("42"), "42 42")
'''
#我的超长答案，先把他转成列表，再那个唉
#134ms
def high_and_low(numbers):
	panduan = list(numbers)
	length = len(panduan)
	d = []
	for i in range(length):
		d.append('')
	j = 0
	for i in range(length):
		if panduan[i] != ' ':
			d[j] = d[j]+ panduan[i]
		else:
			j +=1
			continue
	for i in range(len(d)):
		if d[i] != '':
			continue
		else:
			d = d[:i]
			break
	for i in range(len(d)):
		d[i] = int(d[i])
	high = max(d)
	low = min(d)
	num = str(high)+' '+str(low)
	return num
  
  #好答案，然而我的代码整体比这个快，不知为何？
  def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
