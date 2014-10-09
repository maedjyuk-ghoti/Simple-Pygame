import sys
import pygame
import random
import player
import parallax
import bullet
import factory
import mine
import explosion

class GameManager(object):
    def __init__(self, screen):
        self.screen = screen
        self.ticks = pygame.time.get_ticks()
        pygame.mouse.set_visible(False)
        self.elapsed = 0
        self.delay = 5
        self.cur_ticks = pygame.time.get_ticks()
        self.keys = pygame.key.get_pressed()
        self.frames = 0
        self.first_run = True

        #These need to be changeable through options menu eventually
        self.player_key_up = pygame.K_UP
        self.player_key_shoot = pygame.K_SPACE

        self.factory = factory.Factory(screen, ("player", "player_star.png"),
                ("bullet", "bullet.png"), ("mine", "brown_mine.png"))

        self.background = parallax.ParallaxSurface((640, 480))
        self.background.add("images/background_far.png", 2)
        self.background.add("images/background_close.png", 1)

        self.explosions = []

        self.player = player.Player()

        #Bullet stuffs (with pooling)
        self.bullets = []
        self.bullet_delay = 300
        self.bullet_cur_ticks = self.cur_ticks
        self.bullet_elapsed = 0

        #Enemy creation
        self.enemy_group = pygame.sprite.Group()
        self.num_enemies = 0
        while self.num_enemies < random.randint(20, 40):
            self.num_enemies += 1
            self.enemy_group.add(mine.Mine(random.randint(960, 1560),
                        random.randint(20, 460),
                        random.randint(-7, -3), 0))

    def on_exit(self):
        """ Function to perform at end of program """
        ticks = pygame.time.get_ticks() - self.ticks
        print "GAME OVER"
        print "mines:", self.num_enemies
        print "frames:", self.frames
        print "ticks:", ticks
        print "fps:", self.frames/(ticks*0.001)
        self.first_run = True
        # Save whatever needs saving from the gamescreen (score most likely)
        # need a way to go back to the main menu or just stop entirely
        # in a more glorious/graceful way than the this
        sys.exit()

    def shoot(self):
        """ Performs all creation and procedures needed to shoot a bullet """
        prev_ticks = self.bullet_cur_ticks
        self.bullet_cur_ticks = pygame.time.get_ticks()
        ticks = self.bullet_cur_ticks - prev_ticks
        self.bullet_elapsed += ticks
        if self.bullet_elapsed > self.bullet_delay:
            fired = False
            player_loc = self.player.get_loc()
            player_size = self.player.get_size()
            player_mid_right = ((player_loc[0] + player_size[0]),
                    (player_loc[1] + (player_size[1]/2)))

            for bul in self.bullets:
                if not bul.is_on_screen():
                    b_size = bul.get_size()
                    b_loc = ((player_mid_right[0] - (b_size[0]/2)),
                        (player_mid_right[1] - (b_size[1]/2)))
                    bul.shoot(b_loc)
                    fired = True
                    break

            if not fired:
                bul = bullet.Bullet()
                b_size = bul.get_size()
                b_loc = ((player_mid_right[0]),
                    (player_mid_right[1] - (b_size[1]/2)))
                bul.shoot(b_loc)
                self.bullets.append(bul)
            self.bullet_elapsed = self.bullet_elapsed % self.bullet_delay

    def display(self):
        """ Called from manager, handles draws and updates of all assets """
        if self.first_run:
            self.ticks = pygame.time.get_ticks()
            self.first_run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.on_exit()

        prev_ticks = self.cur_ticks
        self.cur_ticks = pygame.time.get_ticks()
        ticks = self.cur_ticks - prev_ticks
        self.elapsed += ticks
        if self.elapsed > self.delay:
            self.elapsed = self.elapsed % self.delay
            self.keys = pygame.key.get_pressed()

        if self.keys[self.player_key_up]:
            self.player.move_up()
        if self.keys[self.player_key_shoot]:
            self.shoot()

        self.background.scroll(2)
        self.player.update()
        self.enemy_group.update()
        for bul in self.bullets:
            if bul.is_on_screen:
                bul.update()

        self.background.draw(self.screen)
        self.player.draw()
        self.enemy_group.draw(self.screen)

        if pygame.sprite.spritecollide(self.player, self.enemy_group, True):
            print "YOU WERE HIT"
            self.on_exit()

        for bul in self.bullets:
            if bul.is_on_screen:
                bul.draw()
                enemies = pygame.sprite.spritecollide(bul,
                        self.enemy_group, True)
                if enemies:
                    bul.hit()
                    for enemy in enemies:
                        exploded = explosion.Explosion(enemy.image,
                            enemy.rect, enemy.x, enemy.y, enemy.speed_x/4.0)
                        self.explosions.append(exploded)
        if len(self.explosions):
            for exploding in self.explosions:
                exploding.update()
                exploding.draw()

        if not len(self.enemy_group):
            temp_explosions = []
            for exploding in self.explosions:
                if not exploding.done:
                    temp_explosions.append(exploding)
            self.explosions = temp_explosions
            if not len(self.explosions):
                print "YOU WIN"
                self.on_exit()

        pygame.display.flip()
        self.frames += 1


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.set_caption('GameManager Test')
    gamemanager = GameManager(screen)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        gamemanager.display()

