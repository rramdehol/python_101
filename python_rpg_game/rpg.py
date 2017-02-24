from random import randint
from os import system
# import hero
from rpg_hero import Hero;
from rpg_monsters import Goblin;

hero = Hero();
enemies = [Goblin()]

for enemy in enemies:
	# Loop through all the bad guys in the enemies list
	print vars(enemy)
	# while hero.health  > 0 and enemy.health > 0:
	while hero.alive() and enemy.alive():
		print 'What will you do?';
		print '1. Fight %s'% enemy.name
		print '2. Run Away';
		print '>',
		input = raw_input();
		if int(input) == 1:
			# user has choosen to fight
			# subtract helath from enemy = hero power
			# enemy.health -= hero.power;
			hero.attack(enemy);
		elif int(input)==2: 
			# usr has choose to run away
			break;
		else: 
			print 'Invalid Choice %r' % input;
		if enemy.alive() > 0:
			# User has made their choice and now its the enemies turn
			# If the enemy has health. Subtract his power from hero health
			# hero.health -= enemy.power;
			enemy.attack(hero);
			number = randint(1,5);
			print number;
			# number = 3;
        	if (number == 3):
        		hero.medic_powerup();
	if hero.alive() > 0:
		# we know they won cause someones health is zero
		print 'You won! The %s is defeated' % enemy.name
		system("say v=Zarvox 'You won the monster is defeated'")
	else: 
		# we know the hero lost. because someone won and it
		print 'You were defeated by the ferocious %s' %enemy.name
