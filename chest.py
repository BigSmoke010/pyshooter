import pygame

class chest(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('./images/chest/chestclosed.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(topleft=[370, 500])

    def chestopen(self):
        self.image = pygame.image.load('./images/chest/chestopen.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))

    def chestclose(self):
        self.image = pygame.image.load('./images/chest/chestclosed.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))