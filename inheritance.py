class Animal(object):
	def __init__(self,name, species):
		self.name = name;
		self.species = species;
	def speak(self):
		print self.name + " is making a noise";
	def run(self):
		print self.name + " is running";

animal1 = Animal("Mitzie","Alien");
animal1.speak();
animal1.run();

# Make a new class instead of passing object or nothing 
# pass then name  of the parent class
class Dog(Animal):
	def __init__(self, dog_name):
		Animal.__init__(self, dog_name, self);
		print self.name;
dog = Dog("Fido");
print dog.speak();
print dog.species;
