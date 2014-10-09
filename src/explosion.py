from helpers import *
from random import randint
import random

CHUNKS = 16
EXPLODE_SPEED = 0.0

class Chunk(pygame.sprite.Sprite):
  def __init__(self, image, sx, sy, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.screen = pygame.display.get_surface()
    self.image = image
    self.rect = image.get_rect()
    self.x, self.y = x, y
    self.speedx, self.speedy = sx, sy
    self.rect.topleft = (self.x, self.y)
    self.curr_ticks = pygame.time.get_ticks()

  def update(self):
    prev_ticks = self.curr_ticks
    self.curr_ticks = pygame.time.get_ticks()
    ticks = self.curr_ticks - prev_ticks
    self.speedy += 0.005
    incrx = self.speedx * ticks
    incry = self.speedy * ticks
    self.x += incrx
    self.y += incry
    if self.y >= self.screen.get_rect().height:
      self.kill()
    self.rect.topleft = (self.x, self.y)


class Explosion(pygame.sprite.Sprite):
  def __init__(self, image, rect, x, y, speed):
    pygame.sprite.Sprite.__init__(self)
    self.image, self.rect = image, rect
    self.x, self.y = x, y
    self.speedx = speed
    self.screen = pygame.display.get_surface()
    self.screenRect = self.screen.get_rect()
    self.chunkGroup = pygame.sprite.Group()
    self.makeChunks()
    self.done = False

  # Ternary operator: 'a'if 1 == 0 else 'b'
  def makeChunks(self):
    n = CHUNKS
    chunk_width = self.rect.width/n
    chunk_height = self.rect.height/n
    imgSize = (chunk_width, chunk_height)
    for i in xrange(n):
      for j in xrange(n):
        sx=(random.random()+EXPLODE_SPEED) * (-1 if randint(1,2)==1 else 1)
        sx += self.speedx
        sy=(random.random()+EXPLODE_SPEED) * (-1 if randint(1,2)==1 else 1)
        x = i * chunk_width
        y = j * chunk_width
        tmpImg = pygame.Surface(imgSize)
        #tmpImg.fill(pygame.Color("magenta"))
        tmpImg.blit(self.image, (0, 0), ((x, y), imgSize))
        tmpImg.set_colorkey(pygame.Color("magenta"))
        self.chunkGroup.add( Chunk(tmpImg, sx, sy, x+self.x, y+self.y) )

  def update(self):
    self.chunkGroup.update()
    if len(self.chunkGroup) == 0: self.done = True

  def draw(self):
    self.chunkGroup.draw(self.screen)

