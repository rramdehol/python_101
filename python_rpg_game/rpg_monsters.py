from Character import Character
class Goblin(Character):
	def __init__(self):
		Character.__init__(self)
		self.name = 'goblin';
		self.health = 6;
		self.power = 2;
	# def alive(self):
	# # return a boolean will simply be true IF monster health is >0 false if health is <0 
	# return self.health > 0;
	# def take_damage(self, points_of_damage):
	# 	self.health -= points_of_damage;
	# def attack(self, hero):
	# 	print '%s attacks %s' % (self.name, hero.name)
	# 	hero.take_damage(self.power);

