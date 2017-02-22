from zombie import Zombie
from hero import Hero

# make a zombie object from class
zombie_object = Zombie(6,8,19,'bat',15);
print zombie_object.strength;
# ugly version of print
print dir(zombie_object);
print vars(zombie_object);

# Make a hero object from the hero class
hero1 = Hero();
Hero.cheer_hero(hero1);