#Input one
array1 = ['magical unicorns',19,'hello',98.98,'world']
array2 = [2,3,1,7,4,12]
array3 = ['magical','unicorns']

def list_type(obj):

    new_string = ""
    total = 0
    for i in obj:
        if type(i) == int:
            total += i
        elif type(i) == str:
            new_string = new_string + i + " "

    if total != 0 and new_string != "":
        print "The list you entered is of mixed type"
        print "String: ", new_string
        print "Sum: ", total

    elif total != 0:
        print "The list you entered is of integer type"
        print "Sum: ", total

    elif new_string != "":
        print "The list you entered is of string type"
        print "String: ", new_string

print list_type(array1)
print list_type(array2)
print list_type(array3)
