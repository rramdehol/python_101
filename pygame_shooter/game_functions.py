# A file for all our game functions to clean up main.pygame
import pygame;
# We need sysy to hault the program
import sys;
# get our Hero class
from hero import Hero;

def check_events(hero, start_button, game_settings):
	for event in pygame.event.get():
		# This means the user clicked on the red X
		if event.type == pygame.QUIT:
			# Stop the game the user wants off
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			print event.key
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos();
			# check for key press right arrow
			if start_button.rect.collidepoint(mouse_x, mouse_y):
				game_settings.game_active = True;
				# bg_music = pygame.mixer.Sound('faf.wav')
				# bg_music.play();
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