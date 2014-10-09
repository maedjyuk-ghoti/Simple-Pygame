
import helpers

class Factory(object):
	__sprites = {}
	__screen = None
	def __init__(self, screen = None, *args):
		if screen:
			Factory.__screen = screen

		for f in args:
			#f[0] = name to refer to it by
			#f[1] = filename
			if isinstance(f[1], str):
				#make a sprite for it
				#load it into a dictionary with f[1] as the key
				Factory.__sprites[f[0]] = helpers.load_image(f[1])
			else:
				#not a filename, don't care
				pass

	def get_sprite_data(self, key):
		try:
			return Factory.__sprites[key]
		except KeyError:
			print "Key: ", key, "doesn't exist"

	def get_screen(self):
		return Factory.__screen

	def add_sprites(self, *args):
		for f in args:
			#f[0] = name to refer to it by
			#f[1] = filename
			if isinstance(f[1], str):
				#make a sprite for it
				#load it into a dictionary with f[1] as the key
				Factory.__sprites[f[0]] = helpers.load_image(f[1])
			else:
				#not a filename, don't care
				pass
