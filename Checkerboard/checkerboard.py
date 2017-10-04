def check_bd(col, row):
    x = ""
    y = ""
    for i in range(0, col):
        x = x + "* "
        y = y + " *"

    for j in range(0, row):
        print x
        print y


check_bd(4, 4)
