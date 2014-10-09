import pygame
import os
import sys
import helpers
import factory

MIN_SPIN = 1.0
DELAY = 20

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = "player"

        #Get these from xml
        self.image_size = (60, 30)
        self.frames = 4
        self.speed_x = 0
        self.speed_y = 0
        self.delta_y = 3

        #Probably shouldn't touch these
        pygame.sprite.Sprite.__init__(self)
        self.imgList = []
        self.loadImages()
        self.image = self.imgList[0]
        self.rect = self.image.get_rect()
        self.screen = factory.Factory().get_screen()
        self.screenRect = self.screen.get_rect()
        self.x = self.rect.width/2
        self.y = self.screenRect.height/2 - self.rect.height/2
        self.rect.topleft = (self.x, self.y)
        self.curr_ticks = pygame.time.get_ticks()
        self.delay = 0
        self.index = 0
        self.moving_up = False

    def loadImages(self):
        imgMaster = factory.Factory().get_sprite_data(self.image_file)
        offset = []
        for i in range(self.frames):
            offset.append((i * self.image_size[0], 0))
            tmpImg = pygame.Surface(self.image_size)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], self.image_size))
            transColor = tmpImg.get_at((0,0))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)

    def move_up(self):
        self.moving_up = True

    def explode(self):
        print "BOOM!"

    def get_size(self):
        return (self.rect.width, self.rect.height)

    def get_loc(self):
        return (self.x, self.y)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        prev_ticks = self.curr_ticks
        self.curr_ticks = pygame.time.get_ticks()
        ticks = self.curr_ticks - prev_ticks

        incry = self.speed_y * ticks
        incrx = self.speed_x * ticks
        self.delay += (abs(incrx) + abs(incry) + MIN_SPIN)
        if self.delay > DELAY:
            self.index = (self.index + 1) % self.frames
            self.delay = 0
        self.image = self.imgList[self.index]

        if self.moving_up:
            self.y -= self.delta_y
            if self.y < 0:
                self.y = 0
            self.moving_up = False
        else:
            self.y += self.delta_y
            if self.y > self.screenRect.height - self.rect.height:
                self.y = self.screenRect.height - self.rect.height

        self.rect.topleft = (self.x, self.y)
