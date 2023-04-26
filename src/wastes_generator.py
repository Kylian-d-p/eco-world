import pygame
from waste import Waste
import random


class WastesGenerator(pygame.sprite.Sprite):

    def __init__(self, screen_height) -> None:
        super().__init__()
        apple = pygame.image.load(
            "assets/wastes/apple.PNG").convert_alpha()
        bottle = pygame.image.load(
            "assets/wastes/bottle.PNG").convert_alpha()
        cigarette = pygame.image.load(
            "assets/wastes/cigarette.PNG").convert_alpha()
        newspaper = pygame.image.load(
            "assets/wastes/newspaper.PNG").convert_alpha()

        dimensions_list = [[apple.get_width(), apple.get_height()], [bottle.get_width(), bottle.get_height(
        )], [cigarette.get_width(), cigarette.get_height()], [newspaper.get_width(), newspaper.get_height()]]
        # Itérer la boucle pour réduire chaque couple de dimensions à max 50x50 en gardant le ratio
        for i in range(len(dimensions_list)):
            while dimensions_list[i][0] > 50 or dimensions_list[i][1] > 50:
                dimensions_list[i][0] /= 1.2
                dimensions_list[i][1] /= 1.2

        self.wastes: list[pygame.Surface] = [
            pygame.transform.smoothscale(
                apple, (dimensions_list[0][0], dimensions_list[0][1])).convert_alpha(),
            pygame.transform.smoothscale(
                bottle, (dimensions_list[1][0], dimensions_list[1][1])).convert_alpha(),
            pygame.transform.smoothscale(
                cigarette, (dimensions_list[2][0], dimensions_list[2][1])).convert_alpha(),
            pygame.transform.smoothscale(
                newspaper, (dimensions_list[3][0], dimensions_list[3][1])).convert_alpha()
        ]
        self.wastes_group: pygame.sprite.Group = pygame.sprite.Group()
        self.wastes_height: int = screen_height - 100

    def generate_waste(self, screen: pygame.Surface, is_flying: bool=False, flying_speed: int=False) -> None:
        """
        Génère un déchet à une position aléatoire sur l'axe des x
        """
        if is_flying:
            height = random.randint(0, self.wastes_height - 100)
        else:
            height = self.wastes_height
        waste = Waste(self.wastes[random.randint(0, len(self.wastes) - 1)], screen.get_width(), height, is_flying, flying_speed)
        self.wastes_group.add(waste)

    def update(self, screen: pygame.Surface, player_speed: int) -> None:
        """
        Mets à jour la position des déchets et en génère aléatoirement
        """
        self.wastes_group.update(player_speed)

        self.wastes_group.draw(screen)

        if random.randint(0, 40) == 0:
            self.generate_waste(screen)
        elif random.randint(0, 50) == 0:
            self.generate_waste(screen, True, random.randint(5, 15))

    def collided(self, sprite: pygame.sprite.Sprite) -> None:
        """
        Supprime tous les déchets sauf le sprite passé en paramètre
        """
        for waste in self.wastes_group:
            waste.collided(sprite)
