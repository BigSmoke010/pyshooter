import pygame
import characters
import map
import chest
import weapons
from random import randint

class loop:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,600))
        self.map = map.pyMap()
        self.game = 1
        self.last = pygame.time.get_ticks()
        self.char1 = characters.character(1)
        self.char2 = characters.character(2)
        self.char1wp = weapons.char1weapon(10, False)
        self.char2wp = weapons.char2weapon(10, False)
        self.chest = chest.chest()
        self.xforchar1 = 0
        self.xforchar2 = 0
        self.gravityforchar1 = 0
        self.gravityforchar2 = 0
        self.char1state = 'right'
        self.char2state = 'left'
        self.alljumpsforchar1 = 0
        self.alljumpsforchar2 = 0
        self.x = any
        self.y = any
        self.char1stand = True
        self.char2stand = True
        self.shot1 = False
        self.shot2 = False
        self.showchest = False
        self.chestopen = False
        self.char1slash = False
        self.char2slash = False
        self.char2hit = False
        self.char1hit = False
        self.plyr1health = 100
        self.plyr2health = 100
        self.healthimg =  pygame.image.load('./images/healthbar.png').convert_alpha()
        self.healthimg = pygame.transform.scale(self.healthimg,(212, 35))
        self.healthimg2 = pygame.transform.flip(self.healthimg, True, False)
        self.healthbar1 = pygame.rect.Rect(10, 50, self.plyr1health * 2, 25)
        self.healthbar2 = pygame.rect.Rect(590, 50, self.plyr2health * 2, 25)
        self.usrevnt = pygame.USEREVENT + 1
        self.timer = pygame.time.set_timer(self.usrevnt, 10_000)
        self.gottime = False
        self.charsgroup = pygame.sprite.Group()
        self.chestsgroup = pygame.sprite.Group()
        self.chestsgroup.add(self.chest)
        self.charsgroup.add(self.char1)
        self.charsgroup.add(self.char2)
        self.font = pygame.font.Font('./fonts/VCR_OSD_MONO_1.001.ttf', 30)
        self.font2 = pygame.font.Font('./fonts/Spaceship Bullet.ttf', 25)
        self.running = True

    def startloop(self):
        while self.running:
            self.screen.fill((0,0,0))
            self.map.showmap(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.usrevnt and not self.showchest and randint(0,1):self.showchest = True
                if event.type == pygame.KEYDOWN:
                    if self.game == 1:
                        if event.key == pygame.K_UP and self.alljumpsforchar2 < 2:
                            self.gravityforchar2 = -20
                            self.alljumpsforchar2 += 1
                        if event.key == pygame.K_LEFT:
                            self.xforchar2 = -10
                            self.char2stand = False
                            self.char2state = 'left'
                        if event.key == pygame.K_RIGHT:
                            self.xforchar2 = 10
                            self.char2stand = False
                            self.char2state = 'right'
                        if event.key == pygame.K_DOWN:
                            self.shot2 = True
                            self.x = self.char2.rect.x
                            self.y = self.char2.rect.y + 10
                            if self.char2wp.type != 'mele':
                                self.char2wp.bullets.append((pygame.rect.Rect(self.x, self.y, 25, 25), self.char2state))
                                self.char2wp.shootdetach(self.char2.rect.x, self.char2.rect.y, self.shot2)
                            self.char2wp.shoot(self.screen, self.char2state, self.char2.rect.x, self.char2.rect.y)
                            self.char2wp.allshots += 1 
                            if self.char2wp.allshots == self.char2wp.ammo:
                                self.char2wp = weapons.char2weapon(10, False)
                            self.char2slash = True
                            self.char1hit = False

                        if event.key == pygame.K_w and self.alljumpsforchar1 < 2:
                            self.gravityforchar1 = -20
                            self.alljumpsforchar1 += 1
                        if event.key == pygame.K_d:
                            self.xforchar1 = 10
                            self.char1stand = False
                            self.char1state = 'right'
                        if event.key == pygame.K_a:
                            self.xforchar1 = -10
                            self.char1stand = False
                            self.char1state = 'left'
                        if event.key == pygame.K_s:
                            self.shot1 = True
                            self.x = self.char1.rect.x
                            self.y = self.char1.rect.y + 10
                            if self.char1wp.type != 'mele':
                                self.char1wp.bullets.append((pygame.rect.Rect(self.x, self.y, 25, 25), self.char1state))
                                self.char1wp.shootdetach(self.char1.rect.x, self.char1.rect.y, self.shot1)
                            self.char1wp.shoot(self.screen, self.char1state, self.char1.rect.x, self.char1.rect.y)
                            self.char1wp.allshots += 1 
                            if self.char1wp.allshots == self.char1wp.ammo:
                                self.char1wp = weapons.char1weapon(10, False)
                            self.char1slash = True
                            self.char2hit = False

                    if self.game == 2:
                        if event.key == pygame.K_r:
                            self.char1wp = weapons.char1weapon(10, False)
                            self.char2wp = weapons.char2weapon(10, False)
                            self.plyr1health = 100
                            self.plyr2health = 100
                            self.char1.rect.x = 100
                            self.char2.rect.x = 600
                            self.char1.rect.y = 1
                            self.char2.rect.y = 1
                            self.char1.indx = 0
                            self.char2.indx = 0
                            self.char1.tmplist.clear()
                            self.char2.tmplist.clear()
                            self.char1wp.bullets.clear()
                            self.char2wp.bullets.clear()
                            self.game = 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        if self.xforchar1 == 10:
                            self.char1stand = True
                            self.xforchar1 = 0
                    if event.key == pygame.K_a:
                        if self.xforchar1 == -10:
                            self.char1stand = True
                            self.xforchar1 = 0

                    if event.key == pygame.K_RIGHT :
                        if self.xforchar2 == 10:
                            self.char2stand = True
                            self.xforchar2 = 0
                    if event.key == pygame.K_LEFT:
                        if self.xforchar2 == -10:
                            self.char2stand = True
                            self.xforchar2 = 0

            if self.game == 1:
                pygame.draw.rect(self.screen, 'red', self.healthbar1)
                pygame.draw.rect(self.screen, 'red', self.healthbar2)
                self.screen.blit(self.healthimg, (0,45))
                self.screen.blit(self.healthimg2, (590,45))
                self.screen.blit(pygame.transform.scale(self.char1wp.bulletimg, (25,25)), (230, 46))
                self.screen.blit(pygame.transform.scale(self.char2wp.bulletimg, (25,25)), (550, 46))
                if self.char2wp.ammo:
                    self.screen.blit(self.font2.render(str(self.char2wp.ammo - self.char2wp.allshots) + '/' + str(self.char2wp.ammo), False, 'black'), (760, 100))
                if self.char1wp.ammo:
                    self.screen.blit(self.font2.render(str(self.char2wp.ammo - self.char2wp.allshots) + '/' + str(self.char2wp.ammo), False, 'black'), (0, 100))
                self.healthbar1.width = self.plyr1health * 2
                self.healthbar2.width = self.plyr2health * 2

                self.char1.rect.x += self.xforchar1
                self.char2.rect.x += self.xforchar2

                self.gravityforchar2 += 1
                self.gravityforchar1 += 1

                self.char1.rect.y += self.gravityforchar1
                self.char2.rect.y += self.gravityforchar2

                if self.char1slash:
                    if not self.char1wp.shoot(self.screen, self.char1state, self.char1.rect.x, self.char1.rect.y):
                        self.char1slash = False
                if self.char2slash:
                    if not self.char2wp.shoot(self.screen, self.char2state, self.char2.rect.x, self.char2.rect.y):
                        self.char2slash = False

                if self.showchest:
                    self.chestsgroup.draw(self.screen)
                if self.char1.rect.colliderect(self.chest) and self.showchest:
                    self.chest.chestopen()
                    self.char1wp = weapons.sword(20, 5)
                    self.chestopen = True
                if self.char2.rect.colliderect(self.chest) and self.showchest:
                    self.chest.chestopen()
                    self.char2wp = weapons.sword(20, 5)
                    self.chestopen = True
                if self.showchest and self.chestopen:
                    now = pygame.time.get_ticks()
                    if not self.gottime:
                        self.getlasttime(now)
                    if now - self.last >= 3000:
                        self.showchest = False
                        self.chestopen = False
                        self.chest.chestclose()
                        self.gottime = False

                if self.char1wp.type != 'mele':
                    self.char1wp.shoot(self.screen, self.char1state)
                else:
                    if self.char2.rect.colliderect(self.char1wp.rect) and not self.char2hit:
                        self.plyr2health -= 10
                        self.char2hit = True
                if self.char2wp.type != 'mele':
                    self.char2wp.shoot(self.screen, self.char2state)
                else:
                    if self.char1.rect.colliderect(self.char2wp.rect) and not self.char1hit:
                        self.plyr1health -= 10
                        self.char1hit = True
                self.charsgroup.draw(self.screen)               
                for img, block in self.map.allblocks:
                    for bullet,d in self.char1wp.bullets:
                        if bullet.colliderect(block):
                            self.char1wp.bullets.pop(self.char1wp.tmplist.index(bullet))
                            self.char1wp.tmplist.remove(bullet)
                        if bullet.colliderect(self.char2.rect):
                            self.screen.blit(pygame.image.load('./images/skeleton/idle_hit.png').convert_alpha(), self.char2.rect)
                            self.char1wp.bullets.pop(self.char1wp.tmplist.index(bullet))
                            self.char1wp.tmplist.remove(bullet)
                            self.plyr2health -= 10
                    for bullet,d in self.char2wp.bullets:
                        if bullet.colliderect(block):
                            self.char2wp.bullets.pop(self.char2wp.tmplist.index(bullet))
                            self.char2wp.tmplist.remove(bullet)
                        if bullet.colliderect(self.char1.rect):
                            self.screen.blit(pygame.image.load('./images/Player/r_hit_1_hi.png').convert_alpha(), self.char1.rect)
                            self.char2wp.bullets.pop(self.char2wp.tmplist.index(bullet))
                            self.char2wp.tmplist.remove(bullet)
                            self.plyr1health -= 10
                    for i in range(block.left, block.right):
                        if self.char1.rect.collidepoint(i, block.top):
                            self.char1.rect.bottom = block.top
                            self.gravityforchar1 = 0
                            self.alljumpsforchar1 = 0
                        if self.char1.rect.collidepoint(i, block.bottom):
                            self.gravityforchar1 = 0
                            self.char1.rect.top = block.bottom
                        if self.char2.rect.collidepoint(i, block.top):
                            self.char2.rect.bottom = block.top
                            self.gravityforchar2 = 0
                            self.alljumpsforchar2 = 0
                        if self.char2.rect.collidepoint(i, block.bottom):
                            self.gravityforchar2 = 0
                            self.char2.rect.top = block.bottom
                    for i in range(block.top, block.bottom):
                        if self.char1.rect.collidepoint(block.left, i):
                            self.char1.rect.right = block.left
                        if self.char1.rect.collidepoint(block.right, i):
                            self.char1.rect.left = block.right
                        if self.char2.rect.collidepoint(block.left, i):
                            self.char2.rect.right = block.left
                        if self.char2.rect.collidepoint(block.right, i):
                            self.char2.rect.left = block.right
                    for i in range(0, 800):
                        if self.char2.rect.collidepoint(800, i):
                            self.char2.rect.x = 10
                        if self.char1.rect.collidepoint(800, i):
                            self.char1.rect.x = 10
                        if self.char2.rect.collidepoint(0, i):
                            self.char2.rect.x = 750
                        if self.char1.rect.collidepoint(0, i):
                            self.char1.rect.x = 750

                    if self.plyr1health == 0 or self.plyr2health == 0:
                        self.game = 2

                self.charsgroup.update(self.screen, self.char1state, self.char2state, self.char1stand, self.char2stand)
            elif self.game == 2:
                if self.plyr1health == 0:
                    self.char1.death(1, self.screen, self.game)
                    self.rend = self.font.render('PLAYER 2 WINS', False, 'black')
                    self.screen.blit(self.rend, (275, 100))
                    self.rend = self.font.render('PRESS R TO RESTART', False, 'black')
                    self.screen.blit(self.rend, (250, 390))
                else:
                    self.char2.death(2, self.screen, self.game)
                    self.rend = self.font.render('PLAYER 1 WINS', False, 'black')
                    self.screen.blit(self.rend, (275, 100))
                    self.rend = self.font.render('PRESS R TO RESTART', False, 'black')
                    self.screen.blit(self.rend, (250, 390))

            pygame.display.flip()
            self.clock.tick(60)

    def getlasttime(self, x):
        self.last = x
        self.gottime = True
