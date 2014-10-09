import pygame
import os
import sys
import helpers
import factory

class Mine(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = "mine"

        #Get these from xml
        self.image_size = (40, 40)
        self.frames = 2
        self.speed_x = speed_x
        self.speed_y = speed_y

        #Probably shouldn't touch these
        self.img_list = []
        self.load_images()
        self.image = self.img_list[0]
        self.rect = self.image.get_rect()
        self.screen = factory.Factory().get_screen()
        self.screenRect = self.screen.get_rect()
        self.on_screen = False
        self.cur_ticks = pygame.time.get_ticks()
        self.delay = 0
        self.index = 0

        self.x = x
        self.y = y

    def load_images(self):
        """ Loads the frames of an image from a single file """
        img_master = factory.Factory().get_sprite_data(self.image_file)
        offset = []
        for i in range(self.frames):
            offset.append((i * self.image_size[0], 0))
            tmp_img = pygame.Surface(self.image_size)
            tmp_img.blit(img_master, (0, 0), (offset[i], self.image_size))
            trans_color = tmp_img.get_at((0, 0))
            tmp_img.set_colorkey(trans_color)
            self.img_list.append(tmp_img)

    def get_size(self):
        """ returns the tuple with the objects size """
        return (self.rect.width, self.rect.height)

    def is_on_screen(self):
        """ returns true or false """
        return self.on_screen

    def update(self):
        """ updates position and moves back around """
        #adjust the position
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        self.rect.topleft = (self.x, self.y)

        #Find out if we are still on screen
        if self.x < 0:
            self.x += self.screenRect.width + 30
        elif self.x > self.screenRect.width:
            self.on_screen = False
        elif not self.on_screen:
            self.on_screen = True

        #Change image frame if needed
        prev_ticks = self.cur_ticks
        self.cur_ticks = pygame.time.get_ticks()
        ticks = self.cur_ticks - prev_ticks
        incr = self.speed_x * ticks
        self.delay += incr
        if abs(self.delay) > 1000:
            self.index = (self.index + 1) % self.frames
            self.delay = 0
            self.image = self.img_list[self.index]
