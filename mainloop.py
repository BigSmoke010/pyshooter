import pygame
import time
import characters
import map

class loop:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,600))
        self.map = map.pyMap(self.screen)
        self.char1 = characters.character(1)
        self.char2 = characters.character(2)
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
        self.plyr1health = 100
        self.plyr2health = 100
        self.healthbar1 = pygame.rect.Rect(10, 50, self.plyr1health * 2, 15)
        self.healthbar2 = pygame.rect.Rect(550, 50, self.plyr2health * 2, 15)
        self.charsgroup = pygame.sprite.Group()
        self.charsgroup.add(self.char1)
        self.charsgroup.add(self.char2)
        self.running = True

    def startloop(self):
        while self.running:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
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
                        self.char2.bullets.append((pygame.rect.Rect(self.x, self.y, 25, 25), self.char2state))
                        self.char2.shoot(self.screen, self.char2state)
                        self.char2.shootdetach(self.char2.rect.x, self.char2.rect.y, self.shot2)

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
                        self.char1.bullets.append((pygame.rect.Rect(self.x, self.y, 25, 25), self.char1state))
                        self.char1.shoot(self.screen, self.char1state)
                        self.char1.shootdetach(self.char1.rect.x, self.char1.rect.y, self.shot1)

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

            self.map.showmap(self.screen)

            pygame.draw.rect(self.screen, 'red', self.healthbar1)
            pygame.draw.rect(self.screen, 'red', self.healthbar2)
            self.healthbar1.width = self.plyr1health * 2
            self.healthbar2.width = self.plyr2health * 2

            self.char1.rect.x += self.xforchar1
            self.char2.rect.x += self.xforchar2

            self.gravityforchar2 += 1
            self.gravityforchar1 += 1

            self.char1.rect.y += self.gravityforchar1
            self.char2.rect.y += self.gravityforchar2

            self.charsgroup.draw(self.screen)
            self.char1.shoot(self.screen, self.char1state)
            self.char2.shoot(self.screen, self.char2state)

            for img, block in self.map.allblocks:
                for bullet,d in self.char1.bullets:
                    if bullet.colliderect(block):
                        self.char1.bullets.pop(self.char1.tmplist.index(bullet))
                        self.char1.tmplist.remove(bullet)
                    if bullet.colliderect(self.char2.rect):
                        self.screen.blit(pygame.image.load('./images/Player/r_run_2_damaged.png').convert_alpha(), self.char2.rect)
                        self.char1.bullets.pop(self.char1.tmplist.index(bullet))
                        self.char1.tmplist.remove(bullet)
                        self.plyr2health -= 10
                for bullet,d in self.char2.bullets:
                    if bullet.colliderect(block):
                        self.char2.bullets.pop(self.char2.tmplist.index(bullet))
                        self.char2.tmplist.remove(bullet)
                    if bullet.colliderect(self.char1.rect):
                        self.char2.bulletimg = pygame.image.load('./images/skeleton/bone/bone.png')
                        self.screen.blit(pygame.image.load('./images/Player/r_run_2_damaged.png').convert_alpha(), self.char1.rect)
                        self.char2.bullets.pop(self.char2.tmplist.index(bullet))
                        self.char2.tmplist.remove(bullet)
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
                        
            self.charsgroup.update(self.screen, self.char1state, self.char2state, self.char1stand, self.char2stand)
            pygame.display.flip()
            self.clock.tick(60)





