import random

def cointoss(count):
	coin = ""
	head = 0
	tail = 0
	for i in range(count):
		toss = random.randint(1, 2)
		if toss == 1:
			coin = "heads"
			head += 1
		else:
			coin = "tails"
			tail += 1
		print "Attempt #" + str(i) + ": " + "Throwing a coin... It's a " + coin + "! ... Got " + str(head) + "(s) so far and " + str(tail) + "(s) so far"
	print "head is " + str(head)
	print "tail is " + str(tail)

cointoss(10)