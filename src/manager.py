import pygame
import sys
import menu
import inputbox
import gamemanager

pygame.init()

class Manager(object):
	def __init__(self):
		#Pygame initial stuffs
		self.screen = pygame.display.set_mode((640, 480))
		pygame.display.set_caption('Game (in progress)')
		self.ticks = pygame.time.get_ticks()
		self.views = None
		self.curr_view = None
		self.clock = pygame.time.Clock()

	def set_view(self, view):
		if view == 'Back':
			view = 'Main Menu'
		self.curr_view = view

	def add_menuitem(self, menu, item_key, item_attr):
		self.views[menu].add_menuitem(item_key, self.placeholder)
		self.set_view(menu)

	def quit_game(self, *args):
		print "'Quit' was clicked"
		sys.exit()

	def start_game(self, *args):
		print "Starting Game!"

	def placeholder(self, *args):
		print "Placeholder function called from", args

	def play(self):
		#Menus
		mainMenuFuncs = {'Start': self.set_view,
				'High Scores' : self.set_view,
				'Options': self.set_view,
				'Quit': self.quit_game}
		mainMenu = menu.Menu(self.screen,
					mainMenuFuncs.keys(),
					mainMenuFuncs)

		optionsMenuFuncs = {'Controls': self.set_view,
					'Back': self.set_view}
		optionsMenu = menu.Menu(self.screen,
					optionsMenuFuncs.keys(),
					optionsMenuFuncs)

		controlsMenuFuncs = {'Up: Up Arrow': self.placeholder,
					'Shoot: Space Bar': self.placeholder,
					'Back': self.set_view}
		controlsMenu = menu.Menu(self.screen,
					controlsMenuFuncs.keys(),
					controlsMenuFuncs)

		highscoreMenuFuncs = {'Name': self.set_view,
					'Back': self.set_view}
		highscoreMenu = menu.Menu(self.screen,
					highscoreMenuFuncs.keys(),
					highscoreMenuFuncs)

		#Inputbox for High Scores menu, called when 'Name' is clicked
		nameInputBox = inputbox.Inputbox(self.screen, self.add_menuitem,
						"High Scores", "Name")

		theGame = gamemanager.GameManager(self.screen)

		#Workload
		# Note 1: I don't like hardcoding "Main Menu" as the default curr_view, but the
		#  first menu should be the main menu so it doesn't matter much. Just make
		#  sure there is a "Main Menu" in self.views
		#
		# Note 2: These are the views that can be selected by the set_view() function
		#  these are not all the buttons available
		self.views = {'Main Menu': mainMenu,
				'Options': optionsMenu,
				'High Scores': highscoreMenu,
				'Name': nameInputBox,
				'Start': theGame,
				'Controls': controlsMenu}

		mainloop = True
		self.curr_view = "Main Menu"
		#This is the one loop to rule them all.
		# This should pretty much be the last line,
		# any setup for the game should be above this.
		while mainloop:
			self.clock.tick(60)
			self.views[self.curr_view].display()

if __name__ == "__main__":
	manager = Manager()
	manager.play()
