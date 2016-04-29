class Animal(object):
	pass

class Man(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def walk(self):
		return "I am walking"


class Poacher(Man):
	def __init__(self,name,age, *args,  **kwargs):
		Man.__init__(self, name, age)
		self.gun = kwargs.get('gun','AK-47')
		self.loc = kwargs.get('loc','Nairobi')
		self.game_park = kwargs.get('game_park','Tsavo')
		self.fav = kwargs.get('fav','Elephant')

		# print "Args",  args
		# # for args
		# if args[0]:
		# 	self.loc = args[0]
		# if args[1]:
		# 	self.gun = args[1]	


class Tourism(object):
	pass
p = Man('jane', 23)

pc = Poacher('joe', 23, gun='rifle',fav='NNP', loc='Mombasa')
pc = Poacher('joe', 23, 'Nairobi', 'AK-47', gun='rifle',fav='NNP', loc='Mombasa')

print p, pc.walk()
print pc.name, pc.age, pc.fav, pc.loc




