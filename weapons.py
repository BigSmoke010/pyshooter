import pygame
from natsort import natsorted
import os

class weapon:
    def __init__(self, damage, ammo) -> None:
        self.dmg = damage
        self.ammo = ammo
        self.bulletindex = 0
        self.bulletcollision = False
        self.bullets = []
        self.tmplist = []
    def shoot(self, screen , chardir):
        for rect, dir in self.bullets:
            if rect not in self.tmplist:
                self.tmplist.append(rect)
            if dir == 'left':
                rect.x -= 20
                if self.playernum == 1:
                    self.bulletimg = pygame.transform.flip(self.bulletimg, True, False)
            if dir == 'right':
                rect.x += 20
            if rect.x <= 0 or rect.x >= screen.get_width():
                for i in self.tmplist:
                    if i == rect:
                        try:
                            self.bullets.pop(self.tmplist.index(rect))
                            self.tmplist.remove(rect)
                        except IndexError:
                            pass
            screen.blit(self.bulletimg, rect)
        if self.playernum == 2:
            for i in self.char2bullets:
                self.bulletindex += 0.01
                if self.bulletindex >= len(self.char2bullets) - 1:
                    self.bulletindex = 0
                self.bulletimg = self.char2bullets[int(self.bulletindex)]
    def shootdetach(self, x, y, shoted):
        if shoted:
            try:
                self.bullets[-1][0].y = y + 10
            except IndexError:
                pass


class char1weapon(weapon):
    def __init__(self, damage, ammo) -> None:
        super().__init__(damage, ammo)
        self.bulletimg= pygame.image.load('./images/bullet.png').convert_alpha()
        self.playernum = 1

class char2weapon(weapon):
    def __init__(self, damage, ammo) -> None:
        super().__init__(damage, ammo)
        self.char2bullets = []
        for i in natsorted(os.listdir('./images/skeleton/bone/')):
            self.char2bullets.append(pygame.image.load('./images/skeleton/bone/' + i).convert_alpha())
        self.bulletimg = self.char2bullets[self.bulletindex]
        self.rect = self.bulletimg.get_rect()
        self.playernum = 2


