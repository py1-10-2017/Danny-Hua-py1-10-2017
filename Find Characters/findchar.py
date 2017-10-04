word_list = ['hello','world','my','name','is','Anna']

def find_char(input, ch):
    new_list = []
    for i in input:
        for x in i:
            if x == ch:
                new_list.append(i)

    print new_list
find_char(word_list, "o")
