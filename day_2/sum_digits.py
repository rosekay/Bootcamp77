def sum_digits(A):
	""" takes a list A, and returns
		the sum of all the digits in the 
		list e.g. [10,30,45]should returns
		1+0+3+0+4+5
		"""
	total = 0 
	for i in A:
		x = str (i)
		for z in x:
			total += int (z)
		
	return total	
		

print sum_digits ([10,30,45])




