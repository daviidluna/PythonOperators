print(78+90)
print(78-90)
num_w_comm = '{:,}'.format(89898*9898909)
print(num_w_comm)
other_ = '{:,}'.format(203482309+238423482343)
print(other_)
division = '{:,}'.format(8100000000/9)
print(division)

x = 6
x *= 9
print(x)
x = 78
y = 87
print(x == y)
x = 9 
y = 980980980
print(x != y)
x = 67
print (x > 5 and x > 54)
x = 80
print(x > 87 or x < 87)
x = 8 
print(not(x > 4 and x < 9))

y = ['tiger', 'lion']
x = ['tiger', 'lion']
z = x 
print(z is x) #returns true because z is the same object as x
print (x is y) #returns false because x is not the same object as y, even if they have the same content
print (x == y) #to demonstrate the difference between 'is' and '==': this comparison returns true becaues x is equal to y 

x = ['apple', 'banana']
y = ['apple', 'banana']
z = x
print (x is not z)
print (x is not y)
print (x != y) # '!=' is 'not equal to'