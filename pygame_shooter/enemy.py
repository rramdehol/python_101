import pygame;
from pygame.sprite import Sprite;
import math
class Enemy(Sprite):
	def __init__(self, screen, game_settings):
		super(Enemy, self).__init__()
		self.image = pygame.image.load('monster1.png')
		# set the speed
		# self.speed =2;
		# FInd the location and size of the image loaded
		self.rect = self.image.get_rect();
		# find the location and the size of screen
		self.screen_rect = screen.get_rect();
		# Setup the screen
		self.screen = screen;
		# set the center of the image
		self.rect.centery = self.screen_rect.centery;
		self.rect.right = self.screen_rect.right;
		self.speed = 2;

	def update_me(self, hero):
		dx = self.rect.x - hero.rect.x;
		dy = self.rect.y - hero.rect.y;
		dist = math.hypot(dx, dy);
		dx = dx/dist;
		dy = dx/dist;

		self.rect.x -= dx 
		self.rect.y -= dy 

	def draw_me(self):
		self.screen.blit(self.image,self.rect);