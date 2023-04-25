import pygame
from waste import Waste
import random

class WastesGenerator(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.wastes: list[pygame.Surface] = [
            pygame.transform.scale(pygame.image.load("assets/wastes/apple.PNG").convert_alpha(), (50, 50)),
            pygame.transform.scale(pygame.image.load("assets/wastes/bottle.PNG").convert_alpha(), (50, 50)),
            pygame.transform.scale(pygame.image.load("assets/wastes/cigarette.PNG").convert_alpha(), (50, 50)),
            pygame.transform.scale(pygame.image.load("assets/wastes/newspaper.PNG").convert_alpha(), (50, 50)),
        ]
        self.wastes_group: list = []
        self.wastes_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.wastes_height_1: int = 750

    def generate_waste(self, screen: pygame.Surface, speed: int) -> None:
        """
        Génère un déchet à une position aléatoire sur l'axe des x
        """
        waste = Waste(self.wastes[random.randint(0, len(self.wastes) - 1)], speed, screen.get_width(), self.wastes_height_1)
        self.wastes_group.append(waste)
        self.wastes_sprites.add(waste)

    def update(self, screen: pygame.Surface) -> None:
        """
        Mets à jour la position des déchets et en génère aléatoirement
        """
        for waste in self.wastes_group:
            waste.update()
        
        self.wastes_sprites.draw(screen)

        if random.randint(0, 40) == 0:
            self.generate_waste(screen, random.randint(5, 15))
        
        