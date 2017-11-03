class mathdojo(object):
	def __init__(self):
		self.a = 0

	def add(self, *num):
		for i in range(len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for b in num[i]:
					self.a += b
			else:
				self.a += num[i]
		return self

	def subtract(self, *num):
		for i in range(len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for b in num[i]:
					self.a -= b
			else:
				self.a -= num[i]
		return self

	def result(self):
		print self.a

md = mathdojo()
md.add(2).add(2,5).subtract(3,2).result()

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()