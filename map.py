import pygame

class pyMap:
    def __init__(self) -> None:
        self.allblocks = []
        self.num = 0
        self.bg  = pygame.image.load('./images/storyboard6.png').convert()
        self.surf = pygame.Surface((800,600)).convert()
        self.appendblocks()

    def showmap(self, screen):
        screen.blit(self.surf, (0,0))
        self.surf.blit(self.bg, (0,0))
        for image, rect in self.allblocks:
            self.surf.blit(image,rect)

    def appendblocks(self):
        self.image = pygame.image.load('./images/Block_Tiles/A5.png').convert()
        self.imgrct = self.image.get_rect(topleft=(200, 200))
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/A1.png').convert()
        self.imgrct = self.image.get_rect(topleft=(550, 200))
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/bottom.png').convert()
        self.imgrct = self.image.get_rect(topleft=(0, 550))
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/bottom.png').convert()
        self.image = pygame.transform.flip(self.image, False, True)
        self.imgrct = self.image.get_rect(topleft=(0, -10))
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/left.png').convert()
        self.imgrct = self.image.get_rect(topleft=(0, 200))
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/left.png').convert()
        self.imgrct = self.image.get_rect(topleft=(600, 200))
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/height.png').convert()
        self.imgrct = self.image.get_rect(topleft=(0, 350))
        self.allblocks.append((self.image, self.imgrct))
        self.image = pygame.image.load('./images/Block_Tiles/height.png').convert()
        self.imgrct = self.image.get_rect(topleft=(600, 350))
        self.allblocks.append((self.image, self.imgrct))

