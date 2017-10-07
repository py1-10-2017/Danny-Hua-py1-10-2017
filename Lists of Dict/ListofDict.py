name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

name2 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
favorite_animal2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

name3 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal3 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins"]

def listofdict(person, fav):
	nam_animal = zip(person, fav)
	match = dict(nam_animal)
	print match

listofdict(name, favorite_animal)

def unequal_len(person, fav):
	if len(person) >= len(fav):
		nam_animal = zip(person, fav)
		match = dict(nam_animal)
	else:
		nam_animal = zip(fav, person)
		match = dict(nam_animal)
	print match

unequal_len(name2, favorite_animal2)
unequal_len(name3, favorite_animal3)