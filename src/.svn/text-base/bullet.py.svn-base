import pygame
import os
import sys
import helpers
import factory

class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image_key = "bullet"

		#Get these from xml
		self.image_size = (10, 4)
		self.speed_x = 10
		self.speed_y = 0

		#Probably shouldn't touch these
		self.image = factory.Factory().get_sprite_data(self.image_key)
		self.rect = self.image.get_rect()
		self.screen = factory.Factory().get_screen()
		self.screenRect = self.screen.get_rect()
		self.on_screen = False

		self.x = 0
		self.y = 0

	def get_size(self):
		return (self.rect.width, self.rect.height)

	def draw(self):
		self.screen.blit(self.image, (self.x, self.y))

	def update(self):
		self.x = self.x + self.speed_x
		self.rect.topleft = (self.x, self.y)
		if self.x > (self.screenRect.width - self.rect.width):
			self.on_screen = False

	def hit(self):
		self.on_screen = False
		self.x += self.screenRect.width
		self.y += self.screenRect.height

	def shoot(self, loc):
		self.on_screen = True
		self.x = loc[0]
		self.y = loc[1]

	def is_on_screen(self):
		return self.on_screen
