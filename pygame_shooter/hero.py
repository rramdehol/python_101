# Duh
import pygame;
# THis will get the Sprite class from pygame.sprite
# Our hero will be a sprite
from pygame.sprite import Sprite;

class Hero(Sprite):
	# initialize class properties
	def __init__(self, screen):
		super(Hero,self).__init__();
		self.image = pygame.image.load('hero.png')

		self.screen = screen;
		# Creating a rect porp that will be the diemensions of 
		# the image
		# it is available in the the get_rect in the pygame module
		self.rect =  self.image.get_rect();
		# Now that we have the screen object from main 
		# get the size of the screen
		# print self.screen_rect;
		self.screen_rect = screen.get_rect();
		# This will put the hero at the middle of the screen
		self.rect.centery = self.screen_rect.centery
		# This will put the the left side of out hero at the left side
		self.rect.left = self.screen_rect.left;
		# Set up the moving booleans. All are false at init
		self.moving_right = False;
		self.moving_left = False;
		self.moving_up = False;
		self.moving_down = False;
	def update_me(self):
		# if user is pushing left, move my self.rect left
		if self.moving_right: 
			# The hero moving right
			self.rect.centerx += 10
		elif self.moving_left:
			self.rect.centerx -= 10
		if self.moving_up: 
			# The hero moving down
			self.rect.centery -= 10
		elif self.moving_down:
			self.rect.centery += 10
	def draw_me(self):
		self.screen.blit(source = self.image, dest=self.rect)
