def about_yourself(name, age, cob, fav_lan):
	yourself = {}

	yourself["name"] = name
	yourself["age"] = age
	yourself["country of birth"] = cob
	yourself["favorite language"] = fav_lan

	for key,data in yourself.iteritems():
		print "My", key, "is", data

	# print yourself

about_yourself("Danny", "38", "United States", "English")