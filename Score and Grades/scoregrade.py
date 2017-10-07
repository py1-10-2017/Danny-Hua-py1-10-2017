import random
def scoreGrade(count):
	for i in range(0, count):
		random_num = random.randint(60, 100)
		if random_num >= 60 and random_num < 70:
			print "Score: " + str(random_num) + " ; Your grade is D"
		elif random_num >= 70 and random_num < 80:
			print "Score: " + str(random_num) + " ; Your grade is C"
		elif random_num >= 80 and random_num < 90:
			print "Score: " + str(random_num) + " ; Your grade is B"
		else:
			print "Score: " + str(random_num) + " ; Your grade is A"

	print "End of the program. Bye!"

scoreGrade(8)
