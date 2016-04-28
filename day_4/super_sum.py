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
	if not args:
		return 0
	else:
		total = 0
		for x in args:
			total += x
			return total