class product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "sold"
		return self

	def tax(self, tax):
		self.price = self.price * tax + self.price
		return self

	def ret(self, reason):
		if reason == "defective":
			self.price = 0
			self.status = reason
		if reason == "like_new":
			pass
		if reason == "open":
			self.price = self.price - (self.price * .2)
			self.status = reason
		return self

	def display_all(self):
		print "Price: " + str(self.price)
		print "Item name: " + self.item_name
		print "Weight: " + str(self.weight)
		print "Brand: " + self.brand
		print "Status: " + self.status
		return self

product1 = product(200, "something", 15, "Brand X")
product2 = product(200, "something", 15, "Brand X")
product3 = product(200, "something", 15, "Brand X")
product4 = product(200, "something", 15, "Brand X")
product5 = product(200, "something", 15, "Brand X")

product1.ret("open").display_all()
product2.sell().tax(.15).display_all()
product3.ret("defective").display_all()
product4.ret("like_new").display_all()
product5.display_all()
