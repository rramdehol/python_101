# Give the class a name ... Hero
class Hero(object):
	# Call the init method which is bult into classes
	# Pass it self so that we have a this to work with
	def __init__(self):
		self.name = "Incognito"
		self.health = 10;
		self.power = 5;
	# Make an alive method that returns whether the hero is alive or not
	def alive(self):
		# return a boolean will simply be true IF hero is >0 false if health is <0 
		return self.health > 0;
	def take_damage(self):
		
	def attack (self, enemy):
		print '%s attacks %s' % (self.name, enemy.name);
		enemy.take_damage(self.power);
		time.sleep(1.5);
		print '%s has done %d damage to %s' % (self.name, self.power, enemy.name)