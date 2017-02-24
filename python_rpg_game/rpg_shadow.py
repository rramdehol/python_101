from Character import Character
# Give the class a name ... Hero
class Shadow(Character):
	def __init__(self):
		Character.__init__(self)
		self.name = "Shadow"
		self.health = 1;
		self.power = 0;
	