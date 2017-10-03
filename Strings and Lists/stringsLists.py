#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace('day', 'month')

#Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First and Last
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[7]
firstLast = [y[0], y[7]]
print firstLast

#New List
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print 'z = ', z
print len(z)
firstZ = z[0:5]
secondZ = z[5:11]
print firstZ
print secondZ
print [firstZ] + secondZ
