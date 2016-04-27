def funky(a, b):
		"""if string then cconcatenate"""
		if type(a) and type(b) ==str:
			print (a+b)
		"""if int/float then sum"""
		else:
		if type (a) and type(b) ==int or type (a) and type(b) ==float:
			return (a+b)
		else:
			if type(a)and type(b) ==list:
		 	return  list(a+b)
		else:
			if type (a)and type(b) ==dict:
			dict2 =dict(a.items() + b.items()) 
			return dict2
		else: 
			return "invalid"	




 funky('fizz', 'buz')
print funky({"one":"ten" ,"two": "girl"}),({"baby":"boy","big":"cup"})

