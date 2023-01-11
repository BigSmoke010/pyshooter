import pygame
import characters
import map

class loop:
    def __init__(self) -> None:
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
        self.running = True

    def startloop(self):
        while self.running:
            self.screen.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.alljumpsforchar2 <= 2:
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
                        self.char2.shoot(self.screen, self.char2state)

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
                        self.x = self.char1.char.x
                        self.y = self.char1.char.y
                        self.char1.bullets.append((pygame.rect.Rect(self.x, self.y, 50, 50), self.char1state))
                        self.char1.shoot(self.screen, self.char1state)
                        self.char1.shootdetach(self.char1.char.x, self.char1.char.y, self.shot1)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d or event.key == pygame.K_a:
                        self.char1stand = True
                        self.xforchar1 = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.char2stand = True
                        self.xforchar2 = 0

            self.map.showmap(self.screen)
            self.char1.showchar(self.screen, self.char1state, 1, self.char1stand)    
            self.char2.showchar(self.screen, self.char2state, 2, self.char2stand)    

            self.char1.char.x += self.xforchar1
            self.char2.char.x += self.xforchar2

            self.gravityforchar2 += 1
            self.gravityforchar1 += 1

            self.char1.char.y += self.gravityforchar1
            self.char2.char.y += self.gravityforchar2

            self.char1.shoot(self.screen, self.char1state)

            for img, block in self.map.allblocks:
                for i in range(block.left, block.right):
                    if self.char1.char.collidepoint(i, block.top):
                        self.char1.char.bottom = block.top
                        self.gravityforchar1 = 0
                        self.alljumpsforchar1 = 0
                    if self.char1.char.collidepoint(i, block.bottom):
                        self.gravityforchar1 = 0
                        self.char1.char.top = block.bottom
                for i in range(block.top, block.bottom):
                    if self.char1.char.collidepoint(block.left, i):
                        self.char1.char.right = block.left
                    if self.char1.char.collidepoint(block.right, i):
                        self.char1.char.left = block.right
            pygame.display.update()
            self.clock.tick(60)





