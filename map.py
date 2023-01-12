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
        for i in range(0, 800, 50):
            img = pygame.image.load('./images/Block_Tiles/A10.png').convert_alpha()
            imgrect = img.get_rect(topleft=[i, 550])
            screen.blit(img, imgrect)
            self.allblocks.append((img, imgrect))

        for i in range(0, 200, 50):
            img = pygame.image.load('./images/Block_Tiles/A2.png').convert_alpha()
            imgrect = img.get_rect(topleft=[i, 200])
            screen.blit(img, imgrect)
            self.allblocks.append((img, imgrect))
        for i in range(600, 800, 50):
            img = pygame.image.load('./images/Block_Tiles/A2.png').convert_alpha()
            imgrect = img.get_rect(topleft=[i,  200])
            screen.blit(img, imgrect)
            self.allblocks.append((img, imgrect))

        

