class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print "Name: " + self.name
		print "Health: " + str(self.health)

class dog(animal):
	def __init__(self, name, health):
		super(dog, self).__init__(name, health)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

class dragon(animal):
	def __init__(self, name, health):
		super(dragon, self).__init__(name, health)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def display_health(self):
		print "Name: " + self.name
		print "I am a Dragon"

chicken = animal("chicken", 50)
chicken.walk().walk().walk().run().run().display_health()

dog = dog("dog", 50)
dog.walk().walk().walk().run().run().pet().display_health()

dragon = dragon("dragon", 50)
dragon.fly().display_health()
