from datetime import datetime

class call(object):
	callerid = 0
	def __init__(self, name, phone_num, reason):
		call.callerid += 1
		self.name = name
		self.phone_num = phone_num
		self.time = datetime.now()
		self.reason = reason
		self.id = call.callerid

	def display_all(self):
		print "Id: " + str(self.id)
		print "Name: " + self.name
		print "Phone: " + self.phone_num
		print "Time: " + self.time.strftime("%b, %d %Y %I:%M:%S")
		print "Reason: " + self.reason

class callcenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)

	def add(self, call):
		self.calls.append(call)
		return self

	def remove(self):
		self.calls.pop(0)
		return self

	def remove_phone(self, number):
		for x in self.calls:
			if number == x.phone_num:
				self.calls.remove(x)
		return self

	def info(self):
		for x in self.calls:
			print x.display_all()
			print "-----------------------------------"

caller1 = call("John", "555-555-5555", "Complain")
caller2 = call("Mario", "123-456-7890", "Comment")
caller3 = call("Luigi", "987-654-3210", "Thank you")
caller4 = call("Snow", "987-654-4879", "Complain")
caller5 = call("Peach", "987-654-2222", "Comment")
caller6 = call("Toad", "987-654-3333", "Thank you")
callcenter = callcenter()
caller1.display_all()
print "==========================================="
caller2.display_all()
print "==========================================="
caller3.display_all()
print "==========================================="
callcenter.add(caller1).add(caller2).add(caller3).add(caller4).add(caller5).add(caller6).remove().info()
callcenter.remove_phone("987-654-4879").info()
