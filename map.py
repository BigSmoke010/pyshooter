import pygame

class pyMap:
    def __init__(self, screen) -> None:
        self.allblocks = []
        self.num = 0
        for i in range(16):
            img = pygame.image.load('./images/Block_Tiles/A10.png').convert_alpha()
            imgrect = img.get_rect(topleft=[self.num, 550])
            screen.blit(img, imgrect)
            self.allblocks.append((img, imgrect))
            print(self.allblocks)
            self.num += 50
    def showmap(self, screen):
        for image, rect in self.allblocks:
            screen.blit(image,rect)
        

