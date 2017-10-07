
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuples(dict):
	new_dict = []
	for k,d in dict.iteritems():
		my_tuples = (k, d)
		new_dict.append(my_tuples)
	print new_dict

tuples(my_dict)
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
