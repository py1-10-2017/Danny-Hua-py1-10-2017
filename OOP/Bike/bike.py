class bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayinfo(self):
		print "Price of" + " " + str(self.price)
		print "Top Speed of" + " " + str(self.max_speed) + " MPH"
		print "Miles: " + str(self.miles) + " miles"

	def ride(self):
		self.miles = self.miles + 10
		print "Riding" + " " + str(self.miles)
		return self

	def reverse(self):
		if self.miles > 0:
			self.miles = self.miles - 5
			print "Reversing" + " " + str(self.miles)
		else:
			print "Reversing" + " " + str(self.miles)
		return self

speed_bike = bike(300, 60, 10)
mountain_bike = bike(200, 35, 90)
bmx = bike(150, 25, 50)

speed_bike.ride().ride().ride().reverse().displayinfo()
mountain_bike.ride().ride().reverse().reverse().displayinfo()
bmx.reverse().reverse().reverse().displayinfo()
