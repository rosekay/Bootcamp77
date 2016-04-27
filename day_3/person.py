class Person(object):
	#class Variable
	people_count = 0
	def __init__(self, name, age = 0):
		#instance Variable
		self.name = name
		self.age = age
		Person.people_count += 1
		
	def __repr__(self):
		return "<object: {}, {}>".format(self.name, self.age)


	def say_hello(self):
		return "Hello, I am {} and {} y/o".format(self.name, self.age)	