import pygame
import os
from natsort import natsorted

class character(pygame.sprite.Sprite):
    def __init__(self, playernum, playerpic=None) -> None:
        super().__init__()
        self.playernum = playernum
        self.char1imgs = [pygame.image.load('./images/Player/r_run_1.png').convert_alpha(),pygame.image.load('./images/Player/r_run_2.png').convert_alpha(),pygame.image.load('./images/Player/r_run_3.png').convert_alpha(),pygame.image.load('./images/Player/r_run_4.png').convert_alpha(),pygame.image.load('./images/Player/r_run_5.png').convert_alpha(),pygame.image.load('./images/Player/r_run_6.png').convert_alpha(),pygame.image.load('./images/Player/r_run_7.png').convert_alpha(),pygame.image.load('./images/Player/r_run_8.png').convert_alpha(),pygame.image.load('./images/Player/r_run_9.png').convert_alpha(),pygame.image.load('./images/Player/r_run_10.png').convert_alpha(),pygame.image.load('./images/Player/r_run_11.png').convert_alpha(),pygame.image.load('./images/Player/r_run_12.png').convert_alpha(),pygame.image.load('./images/Player/r_run_13.png').convert_alpha(),pygame.image.load('./images/Player/r_run_14.png').convert_alpha(),pygame.image.load('./images/Player/r_run_15.png').convert_alpha(),pygame.image.load('./images/Player/r_run_16.png').convert_alpha(),]
        self.char1idleimgs = [pygame.image.load('./images/Player/r_idle_1.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_2.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_3.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_4.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_5.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_6.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_7.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_8.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_9.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_10.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_11.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_12.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_13.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_14.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_15.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_16.png').convert_alpha(),pygame.image.load('./images/Player/r_idle_17.png').convert_alpha()]
        self.char1deathimgs = [pygame.image.load('./images/Player/r_death_1.png').convert_alpha(),pygame.image.load('./images/Player/r_death_2.png').convert_alpha(),pygame.image.load('./images/Player/r_death_3.png').convert_alpha(),pygame.image.load('./images/Player/r_death_4.png').convert_alpha(),pygame.image.load('./images/Player/r_death_5.png').convert_alpha(),pygame.image.load('./images/Player/r_death_6.png').convert_alpha(),pygame.image.load('./images/Player/r_death_7.png').convert_alpha(),pygame.image.load('./images/Player/r_death_8.png').convert_alpha(),pygame.image.load('./images/Player/r_death_9.png').convert_alpha(),pygame.image.load('./images/Player/r_death_10.png').convert_alpha(),pygame.image.load('./images/Player/r_death_11.png').convert_alpha(),pygame.image.load('./images/Player/r_death_12.png').convert_alpha(),pygame.image.load('./images/Player/r_death_13.png').convert_alpha(),pygame.image.load('./images/Player/r_death_14.png').convert_alpha(),pygame.image.load('./images/Player/r_death_15.png').convert_alpha(),pygame.image.load('./images/Player/r_death_16.png').convert_alpha()]
        self.char2imgs = []
        self.char2idleimgs = []
        self.char2death = []
        for i in natsorted(os.listdir('./images/skeleton/walk/right/')):
            self.char2imgs.append(pygame.image.load('./images/skeleton/walk/right/'+ i).convert_alpha())
        for i in natsorted(os.listdir('./images/skeleton/idle/right/')):
            self.char2idleimgs.append(pygame.image.load('./images/skeleton/idle/right/' + i).convert_alpha())
        for i in natsorted(os.listdir('./images/skeleton/die/right/')):
            self.char2death.append(pygame.image.load('./images/skeleton/die/right/' + i).convert_alpha())
        self.indx = 0
        if self.playernum == 1:
            self.image = self.char1imgs[self.indx]
        elif self.playernum == 2:
            self.image = self.char2imgs[self.indx]
        if self.playernum == 1:
            self.rect = self.image.get_rect(topleft=[100,1])
        elif self.playernum == 2:
            self.rect = self.image.get_rect(topleft=[600,1])
        self.tmplist = []

    def update(self, screen, direction1, direction2, isstanding1, isstanding2):
        if self.playernum == 1:
            direction = direction1
            isstanding = isstanding1
        else:
            direction = direction2
            isstanding = isstanding2

        if not isstanding:
            for i in self.char1imgs:
                self.indx += 0.01
                if self.playernum == 1:
                    if self.indx >= len(self.char1imgs):
                        self.indx = 0
                    if self.playernum == 1:
                        self.image= self.char1imgs[int(self.indx)]
                else:
                    if self.indx >=len(self.char2imgs):
                        self.indx = 0
                    if self.playernum == 2:
                        self.image= self.char2imgs[int(self.indx)]

                if direction == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)
        if isstanding:
            if self.playernum == 1:
                for i in self.char1idleimgs:
                    self.indx += 0.01
                    if self.playernum == 1:
                        if self.indx >= len(self.char1idleimgs):
                            self.indx = 0
                        self.image= self.char1idleimgs[int(self.indx)]
                if direction == 'left':
                    self.image= pygame.transform.flip(self.image, True, False)
            else:
                for i in self.char2idleimgs:
                    self.indx += 0.01
                    if self.indx >= len(self.char2idleimgs):
                        self.indx = 0
                    self.image= self.char2idleimgs[int(self.indx)]
                if direction == 'left':
                    self.image= pygame.transform.flip(self.image, True, False)

    def death(self, num, screen, game):
        if game == 2:
            if num == 2:
                for i in self.char2death:
                    self.indx += 0.01
                    if self.indx >= len(self.char2death):
                        break
                    self.image = self.char2death[int(self.indx)]
                    screen.blit(self.image, self.rect)
            else:
                for i in self.char1deathimgs:
                    self.indx += 0.01
                    if self.indx >= len(self.char1deathimgs):
                        break
                    self.image = self.char1deathimgs[int(self.indx)]
                    screen.blit(self.image, self.rect)
