import pygame;
# We need sysy to hault the program
import sys;
# print "Pygame Found!"
from settings import Settings;
# get out Hero class
from hero import Hero;
# Initialize all the pygame modules
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
hero = Hero(screen);

# This loop will fun forever:
while 1: 
	for event in pygame.event.get():
		# This means the user clicked on the red X
		if event.type == pygame.QUIT:
			# Stop the game the user wants off
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			print event.key
		# check for key press right arrow
			if event.key == pygame.K_RIGHT:
				print 'pressed right'
				hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				print 'pressed left'
				hero.moving_left = True;
			elif event.key == pygame.K_UP:
				print 'pressed up'
				hero.moving_up = True;
			elif event.key == pygame.K_DOWN:
				print 'pressed down'
				hero.moving_down = True;
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				print 'pressed right'
				hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				print 'pressed left'
				hero.moving_left = False;
			elif event.key == pygame.K_UP:
				print 'pressed up'
				hero.moving_up = False;
			elif event.key == pygame.K_DOWN:
				print 'pressed down'
				hero.moving_down = False;
		# Put the fill as the bg color
	screen.fill(game_settings.bg_color);
	# Update the hero booleans
	hero.update_me();
	# Draw the hero
	hero.draw_me();
	# flip the screen = wipe it out
	pygame.display.flip();