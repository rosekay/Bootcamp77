from person import Person
from kenyan import Kenyan
#pep8
#instance vs class variables vs.
#class methods


p = Person('joe', 23)
p2 = Person('jane', 23)
p3 =Person('george', 40)

a = [('jane', 23), ("joe",50), ("jackie", 34), ("jacob", 23),('jee',18), ('josh', 60)]

b = []
for name, age in a:
	person = Person(name, age)
	b.append(person)

for Person in b:
	print (person.say_hello())
	

 
print p.name	
print p.age	
print p2.people_count
print b
print p.say_hello()

k = Kenyan('miguna', 40)
k.probe(20)
print "Is {} corrupt?{}".format(k.name, k.is_corrupt())
print k.say_hello()

print p.corrupt
print k.corrupt

