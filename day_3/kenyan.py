from person import Person

class Kenyan(Person):
	corrupt = False
	def probe(self, corrupt):
		self.corrupt = corrupt
	def is_corrupt(self):
		if self.corrupt:
			return "Yes"
		return "No"	

#for now
k = Kenyan('miguna', 40)
k.probe(20)
print "Is {} corrupt?{}".format(k.name, k.is_corrupt())
print k.say_hello()
