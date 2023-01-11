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
        self.char1state = 'stand'
        self.char2state = 'stand'
        self.running = True

    def startloop(self):
        while self.running:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.gravityforchar2 = -20
                    if event.key == pygame.K_LEFT:
                        self.xforchar2 = -10
                        self.char2state = 'left'
                    if event.key == pygame.K_RIGHT:
                        self.xforchar2 = 10
                        self.char2state = 'right'
                    if event.key == pygame.K_DOWN:
                        self.char2.shoot(self.screen, self.char2state)
                    if event.key == pygame.K_d:
                        self.xforchar1 = 10
                        self.char1state = 'right'
                    if event.key == pygame.K_a:
                        self.xforchar1 = -10
                        self.char1state = 'left'
                    if event.key == pygame.K_s:
                        self.char1.shoot(self.screen, self.char2stat)

            self.map.showmap(self.screen)
            self.char1.showchar(self.screen, self.char1state, 1)    
            self.char2.showchar(self.screen, self.char2state, 2)    
            self.char1.char.x += self.xforchar1
            self.char2.char.x += self.xforchar2
            self.char1.char.y += self.gravityforchar1
            self.char2.char.y += self.gravityforchar2
            self.gravityforchar2 += 1
            self.gravityforchar1 += 1
            pygame.display.update()
            self.clock.tick(60)





