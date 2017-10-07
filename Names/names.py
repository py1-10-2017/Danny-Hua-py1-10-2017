#Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def firstlast(name):
	for i in xrange(len(name)):
		print name[i]["first_name"], name[i]["last_name"]

firstlast(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def students_instructors(name):
    for group in name.iterkeys():
        print group
        for key, data in enumerate(name[group], 1):
            char = 0
            for i in range(len(data["first_name"] + data["last_name"])):
                char += 1
            print str(key) + " - " + data["first_name"] + " " + data["last_name"] + " - " + str(char)


students_instructors(users)