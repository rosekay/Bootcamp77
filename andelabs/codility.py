'''
for i in range (0, 100):
	print i
for i in range (100):
	print i
	'''

'''
factorial = 1 
for i in range (i, n + 1):
	factorial *= 1
'''
'''
n = 7
for i in range (i, n+1):
	for j in range (i):
		print '*',
	print
		
	
	a = 0
	b = 1
while a <= n:
		print a	
	'''

def looped(*args):


    for x in args:
        if len (x) == 2:
            #return "x: {}, y: {}".format(*x)
            for i in x:
                return "x: {}, y: {}".format(*i)



        elif len (x) == 3:

            for i in x:
                return "x: {}, y: {}, z: {} ".format(*i)

        else:
            print "I dont know whats happening"



print looped ([(10,20,30), (10,40), (4,5,50)])	

	