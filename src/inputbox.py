# found at http://www.pygame.org/pcr/inputbox/
# by Timothy Downs, inputbox written for my map editor

# converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:

import pygame
import sys, string

class Inputbox(object):
	def __init__(self, screen, ret_func, ret_func_arg, question, bg_color = (0, 0, 0),
			font = None, font_size = 30, font_color = (255, 255, 255)):
		#arguments
		self.screen = screen
		self.ret_func_arg = ret_func_arg
		self.ret_func = ret_func
		self.question = question
		self.bg_color = bg_color
		self.font_color = font_color

		#other needed things
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont(font, font_size)
		self.response = None
		self.current_string = []

	def get_key(self):
		while True:
			event = pygame.event.poll()
			if event.type == pygame.KEYDOWN:
				return event.key

	def display_box(self, message):
		"Print a message in a box in the middle of the screen"
		self.screen.fill(self.bg_color)
		self.screen.blit(self.font.render(message, 1, self.font_color),
				((self.scr_width / 2) - 100,
				(self.scr_height / 2) - 10))
		pygame.display.flip()

	def display(self):
		pygame.font.init()
		self.display_box(self.question + ": " + string.join(self.current_string, ""))
		inkey = self.get_key()
		if inkey == pygame.K_BACKSPACE:
			self.current_string = current_string[0:-1]
		elif inkey == pygame.K_RETURN:
			self.response = string.join(self.current_string, "")
			self.current_string = []
			self.ret_func(self.ret_func_arg, self.question + ": " + self.response, None)
		elif inkey == pygame.K_MINUS:
			self.current_string.append("_")
		elif inkey <= 127:
			self.current_string.append(chr(inkey - 32))

if __name__ == '__main__':
	def helloworld(*args):
		print "Hello World"
		sys.exit()

	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Inputbox Test")

	myinputbox = Inputbox(screen, helloworld, None, "Name")

	while True:
		myinputbox.display()
