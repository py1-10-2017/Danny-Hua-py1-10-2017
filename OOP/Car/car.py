class car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12

	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed) + " MPH"
		print "Fuel: " + self.fuel
		print "Mileage: " + str(self.mileage) + " miles"
		print "Tax: " + str(self.tax)

ferrari = car(300000, 200, "empty", 25)
civicTypeR = car(33000, 180, "full", 25)
gtr = car(100000, 200, "not full", 25)
bugatti = car(900000, 200, "empty", 25)
fit = car(9000, 90, "full", 25)
mclaren = car(280000, 200, "empty", 25)

ferrari.display_all()
civicTypeR.display_all()
gtr.display_all()
bugatti.display_all()
fit.display_all()
mclaren.display_all()