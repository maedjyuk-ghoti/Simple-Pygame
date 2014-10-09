#!/usr/bin/python

import sys
import pygame
import menuitem

class Menu(object):
	def __init__(self, screen, items, funcs, bg_color = (0, 0, 0),  font = None,
			font_size = 30, font_color = (255, 255, 255)):
		#screen and dimensions needed for more in constructor
		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height

		#Take the items passed in and make them into menuitems
		self.items_passed = items
		self.items = None
		self.create_menuitems()

		#The rest of the arguments
		self.funcs = funcs
		self.bg_color = bg_color
		self.font = pygame.font.SysFont(font, font_size)
		self.font_color = font_color

		#Other things that will be needed
		self.clock = pygame.time.Clock()
		self.mouse_is_visible = True
		self.cur_item = None

	def create_menuitems(self):
		self.items = []
		for index, item in enumerate(self.items_passed):
			menu_item = menuitem.MenuItem(item)
			t_h = len(self.items_passed) * menu_item.height
			pos_x = (self.scr_width / 2) - (menu_item.width / 2)
			pos_y = (self.scr_height / 2) - (t_h / 2) + (index * menu_item.height)
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)

	def add_menuitem(self, item_key, item_attr):
		self.items_passed.append(item_key)
		self.funcs.update({item_key: item_attr})
		self.create_menuitems()

	def set_mouse_selection(self, item, mpos):
		if item.is_mouse_selection(mpos):
			item.set_font_color((255, 0, 0))
			item.set_italic(True)
		else:
			item.set_font_color((255, 255, 255))
			item.set_italic(False)

	def set_mouse_visibility(self):
		if self.mouse_is_visible:
			pygame.mouse.set_visible(True)
		else:
			pygame.mouse.set_visible(False)

	def set_keyboard_selection(self, key):
		for item in self.items:
			item.set_italic(False)
			item.set_font_color((255, 255, 255))

		if self.cur_item is None:
			self.cur_item = 0
		else:
			if key == pygame.K_UP:
				if self.cur_item > 0:
					self.cur_item -= 1
				else:
					self.cur_item = len(self.items) - 1
			elif key == pygame.K_DOWN:
				if self.cur_item < len(self.items) - 1:
					self.cur_item += 1
				else:
					self.cur_item = 0

		self.items[self.cur_item].set_italic(True)
		self.items[self.cur_item].set_font_color((255, 0, 0))

		if key == pygame.K_SPACE or key == pygame.K_RETURN:
			text = self.items[self.cur_item].text
			self.funcs[text](text)

	def display(self):
		self.clock.tick(60)
		mpos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
			if event.type == pygame.KEYDOWN:
				self.mouse_is_visible = False
				self.set_keyboard_selection(event.key)
			if event.type == pygame.MOUSEBUTTONDOWN:
				for item in self.items:
					if item.is_mouse_selection(mpos):
						self.funcs[item.text](item.text)

		if pygame.mouse.get_rel() != (0, 0):
			self.mouse_is_visible = True
			self.cur_item = None

		self.set_mouse_visibility()
		self.screen.fill(self.bg_color)
		for item in self.items:
			if self.mouse_is_visible:
				self.set_mouse_selection(item, mpos)
			self.screen.blit(item.label, item.position)
		pygame.display.flip()

if __name__ == '__main__':
	#When making a function for use in the menu, you need to account for
	# the event being passed, hence the '*args'
	def helloworld(*args):
		print "Hello World"

	#Pygame needs to be init before using anything from pygame
	pygame.init()

	#Give your menu a screen, menus love screens
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('Menu Test')

	#Dictionaries are great here for mapping the 'button' and function togther
	mymenuFuncs = {'Hello World': helloworld,
			'Quit': sys.exit}
	mymenu = Menu(screen, mymenuFuncs.keys(), mymenuFuncs)

	#Give that menu an infinite loop (or else nothing happens)
	while True:
		mymenu.display()
