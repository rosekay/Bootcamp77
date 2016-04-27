def data_type(x):
	"""takes in an argument, x:
		-for an integer, return x ** 2
		-for a float,return x /2
		-for a sring, return "Hello " + x
		-for a boolean, return "boolean"
		-for a long, reurn squareroot(x)
	"""
	
	if type (x) == int:
		return x ** 2
	if type (x)	== float:
		return x / 2
	if type (x) == str:
		return "Hello {}".format(x)
	if type (x) == bool:
		return "boolean"
	if type (x) == long:
		return x ** 0.5
	

print data_type(10.33)
print data_type("rose")
print data_type(100 ** 100)
print data_type(True)
print data_type(45)
print data_type(' s')




