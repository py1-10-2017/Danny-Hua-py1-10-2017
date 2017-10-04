list_a = [1,2,5,6,2]
list_b = [1,2,5,6,2]

list_c = [1,2,5,6,5]
list_d = [1,2,5,6,5,3]

list_e = [1,2,5,6,5,16]
list_f = [1,2,5,6,5]

list_str1 = ['celery','carrots','bread','milk']
list_str2 = ['celery','carrots','bread','cream']

def compare(ls1, ls2):
    if ls1 == ls2:
        print "The lists are the same"
    else:
        print "The lists are not the same."

compare(list_a, list_b)
compare(list_c, list_d)
compare(list_e, list_f)
compare(list_str1, list_str2)
