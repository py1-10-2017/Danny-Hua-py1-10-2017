def oddEven(start, end):
	for i in range(start, end):
		if i % 2 == 0:
			num = "even"
		else:
			num = "odd"

		print "Number is " + str(i) + ". " + "This is an " + num + " number."

oddEven(1, 2000)

def multiply(obj, n):

	for i in xrange(len(obj)):
		obj[i] *= n
	return obj

a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
	layer1 = []
	for i in xrange(len(arr)):
		layer2 = []
		for j in xrange(arr[i]):
			layer2.append(1)
		layer1.append(layer2)
	return layer1


x = layered_multiples(multiply([2,4,5],3))
print x