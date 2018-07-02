#Reverse Integer
class solution(object):
	def reverse1(self,x):
		a =str(x)
		b = list(x for x in a)
		if b[0]== "-":
			c = b[1:]
			c.reverse()
			b[1:] = c
		else:
			b.reverse()
		ls = ''.join(b)
		ls1 = eval(ls)
		if ls1>(2**31-1) or ls1<((-2)**31):
			return 0
		else:
			return ls1

self = solution()
print(self.reverse1(-12435))