from random import randint
class Character(object):
    def __init__(self):
        self.name = '';
        self.health = 0
        self.power = 0
        self.counter = 0
    def alive(self):
		# return a boolean will simply be true IF hero is >0 false if health is <0 
		return self.health > 0;
    def take_damage(self, points_of_damage):
        # self.health -= points_of_damage;
        self.counter += 1;
        if (self.name == 'Shadow' and self.counter ==10):
        	self.health -= 1;
        else:
        	self.health -= points_of_damage;
    def attack(self, character):
        print "%s attacks %s" % (self.name, character.name)
        number = randint(1,5);
        if (number == 3):
        	character.take_damage(self.power*2);
        else:
        	character.take_damage(self.power);