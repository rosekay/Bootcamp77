def super_sum(*args ):
	'''
	return a sum of numbers.
	e.g.
		super_sum() ==>"Please enter a number"
		super_sum(1,2,3) ==> 6
		super_sum([1,2,3]) ==> 6
		super_sum([10], [20,30]) ==> 60
		super_sum("string") ==> 0
	'''
	total = 0	
	if args:
		for x in args:
			if type(x) == list:
				total += sum(x)
			elif type(x) == str:
				return 0
			else:
				total += x
		return total
	return 0			


'''
elif type (args) = list:
		for x in args:
			# x is now ([1, 2, ,3])
			for i in x:
				total += i
			return total
					
			

	else:
		total = 0
		for x in args:
			total += x
			return total
'''			