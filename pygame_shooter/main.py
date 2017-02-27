import pygame;
# print "Pygame Found!"
from settings import Settings;
# get our Hero class
from hero import Hero;
# get our enemy class
from enemy import Enemy;
# Initialize all the pygame modules
from game_functions import check_events;
# from pygame get the sprite stuff and groupcollide
from pygame.sprite import Group, groupcollide
from start_button import Start_Button
pygame.init();
# screen_size = (600,600);
# make a background color
# bg_color = (82,111,53);
# put a message on the status bar so that the player knows 
# the name of the game
pygame.display.set_caption('Monster Attack');
# Create an object out of our settings class
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);

# Make a group for the hero to belong to to use group collide
hero_group = Group()
hero = Hero(screen);
hero_group.add(hero);
enemies = Group();
enemies.add(Enemy(screen, game_settings));
# Make a start button =
start_button = Start_Button(screen);

# This loop will fun forever:
while 1: 
	# run our check_events here!
	check_events(hero, start_button, game_settings);
		# Put the fill as the bg color
	screen.fill(game_settings.bg_color);
	# Update the hero booleans
	for hero in hero_group.sprites():
		hero.update_me();
		# Draw the hero
		hero.draw_me();
	for enemy in enemies.sprites():
		if game_settings.game_active:
			enemy.update_me(hero);
		enemy.update_me(hero);
		enemy.draw_me();
	hero_died = groupcollide(hero_group, enemies, True, True)
	if hero_died:
		print "You Lost!"
	if game_settings.game_active == False:
		start_button.draw_button();

	start_button.draw_button();
	# flip the screen = wipe it out
	pygame.display.flip();