import pygame
import random
from wastes.waste import Waste


class WastesGenerator():

    def __init__(self, screen_height) -> None:
        """
        Constructeur de la classe WastesGenerator
        screen_height: hauteur de l'écran
        """
        # Chargement des images des déchets
        apple = pygame.image.load(
            "assets/wastes/apple.PNG").convert_alpha()
        bottle = pygame.image.load(
            "assets/wastes/bottle.PNG").convert_alpha()
        cigarette = pygame.image.load(
            "assets/wastes/cigarette.PNG").convert_alpha()
        newspaper = pygame.image.load(
            "assets/wastes/newspaper.PNG").convert_alpha()

        # Création d'une liste contenant les dimensions de chaque déchet
        dimensions_list = [[apple.get_width(), apple.get_height()], [bottle.get_width(), bottle.get_height(
        )], [cigarette.get_width(), cigarette.get_height()], [newspaper.get_width(), newspaper.get_height()]]

        # Itérer la boucle pour réduire chaque couple de dimensions à max 50x50 en gardant le ratio
        for i in range(len(dimensions_list)):
            while dimensions_list[i][0] > 50 or dimensions_list[i][1] > 50:
                dimensions_list[i][0] /= 1.2
                dimensions_list[i][1] /= 1.2

        # Transformer les dimensions en entiers
        for i in range(len(dimensions_list)):
            dimensions_list[i][0] = int(dimensions_list[i][0])
            dimensions_list[i][1] = int(dimensions_list[i][1])

        # Création d'une liste contenant les déchets redimensionnés
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
        self.wastes_group: pygame.sprite.Group = pygame.sprite.Group() # Groupe contenant les déchets
        self.wastes_height: int = screen_height - 100 # Hauteur à laquelle les déchets seront générés

    def generate_waste(self, screen: pygame.Surface, is_flying: bool=False, flying_speed: int=False) -> None:
        """
        Génère un déchet à une position aléatoire sur l'axe des x
        screen: surface sur laquelle le déchet sera affiché
        is_flying: si le déchet est un déchet volant
        flying_speed: vitesse du déchet volant
        """
        if is_flying: # Si le déchet est un déchet volant, il sera généré à une hauteur aléatoire entre 100 et la hauteur de l'écran - 100
            height = random.randint(100, self.wastes_height - 100)
        else: # Sinon, il sera généré à la hauteur définie dans le constructeur
            height = self.wastes_height
        waste = Waste(self.wastes[random.randint(0, len(self.wastes) - 1)], screen.get_width(), height, is_flying, flying_speed) # Création du déchet
        self.wastes_group.add(waste) # Ajout du déchet au groupe

    def update(self, screen: pygame.Surface, player_speed: int, is_ground_available: bool , outside_screen_callback) -> None:
        """
        Mets à jour la position des déchets et en génère aléatoirement
        screen: surface sur laquelle les déchets seront affichés
        player_speed: vitesse du joueur
        is_ground_available: Indique si le sol est occupé par un obstacle
        outside_screen_callback: fonction appelée lorsque le déchet sort de l'écran
        """
        self.wastes_group.update(player_speed, outside_screen_callback) # Mise à jour de la position des déchets

        self.wastes_group.draw(screen) # Affichage des déchets

        if is_ground_available:
            if random.randint(0, 40) == 0: # Génération d'un déchet aléatoirement
                self.generate_waste(screen) # Génération d'un déchet
            elif random.randint(0, 50) == 0: # Génération d'un déchet volant aléatoirement
                self.generate_waste(screen, True, random.randint(5, 15)) # Génération d'un déchet volant

    def collided(self, sprite: pygame.sprite.Sprite) -> None:
        """
        Supprime le déchet qui a été touché par le joueur
        sprite: déchet touché par le joueur
        """
        for waste in self.wastes_group: # Itérer la boucle pour trouver le déchet qui a été touché par le joueur
            if waste == sprite: # Si le déchet a été trouvé
                waste.kill() # Suppression du déchet
                break # Sortir de la boucle
