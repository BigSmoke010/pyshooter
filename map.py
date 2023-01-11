import pygame

class pyMap:
    def __init__(self, screen) -> None:
        self.allblocks = []
        self.num = 0
        self.appendblocks(screen)

    def showmap(self, screen):
        for image, rect in self.allblocks:
            screen.blit(image,rect)

    def appendblocks(self, screen):
        self.image = pygame.image.load('./images/Block_Tiles/A5.png').convert_alpha()
        self.imgrct = self.image.get_rect(topleft=(200, 200))
        screen.blit(self.image, self.imgrct)
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/A1.png').convert_alpha()
        self.imgrct = self.image.get_rect(topleft=(550, 200))
        screen.blit(self.image, self.imgrct)
        self.allblocks.append((self.image, self.imgrct))

        for i in range(16):
            img = pygame.image.load('./images/Block_Tiles/A10.png').convert_alpha()
            imgrect = img.get_rect(topleft=[self.num, 550])
            screen.blit(img, imgrect)
            self.allblocks.append((img, imgrect))
            self.num += 50

        self.num = 0
        for i in range(4):
            img = pygame.image.load('./images/Block_Tiles/A2.png').convert_alpha()
            imgrect = img.get_rect(topleft=[self.num, 200])
            screen.blit(img, imgrect)
            self.allblocks.append((img, imgrect))
            self.num += 50

        self.num = 600
        for i in range(4):
            img = pygame.image.load('./images/Block_Tiles/A2.png').convert_alpha()
            imgrect = img.get_rect(topleft=[self.num, 200])
            screen.blit(img, imgrect)
            self.allblocks.append((img, imgrect))
            self.num += 50

        

