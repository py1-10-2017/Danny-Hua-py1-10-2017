#Part I

def draw_stars(arr):
	for i in xrange(len(arr)):
		stars = ""
		for j in range(arr[i]):
			stars += "*"
		print stars

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

# Part II

def mod_draw(arr):
	for i in xrange(len(arr)):
		item = ""
		if type(arr[i]) == int:
			for j in range(arr[i]):
				item += "*"
			print item
		else:
			for j in range(len(arr[i])):
				item += arr[i][0].lower()
			print item

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
mod_draw(y)