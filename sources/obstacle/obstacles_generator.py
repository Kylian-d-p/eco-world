import pygame
from random import randint
from obstacle.obstacle import Obstacle

class ObstaclesGenerator():

    def __init__(self, screen_height):
        """
        Constructeur de la classe ObstaclesGenerator
        screen_height: hauteur de l'écran
        """

        barrel: pygame.Surface = pygame.image.load("assets/obstacles/barrel.PNG").convert_alpha() # Image du tonneau
        car: pygame.Surface = pygame.image.load("assets/obstacles/car.PNG").convert_alpha() # Image de la voiture

        self.obstacles_group: pygame.sprite.Group = pygame.sprite.Group()

        dimensions_list: list[tuple[int, int]] = [ # Liste des dimensions des obstacles
            (barrel.get_width(), barrel.get_height()),
            (car.get_width(), car.get_height())
        ]

        # Itérer la boucle pour réduire chaque couple de dimensions à max 350x350 en gardant le ratio
        for i in range(len(dimensions_list)):
            while dimensions_list[i][0] > 350 or dimensions_list[i][1] > 350:
                dimensions_list[i] = (dimensions_list[i][0] / 1.2, dimensions_list[i][1] / 1.2)


        self.obstacles: list[pygame.Surface] = [ # Liste des obstacles redimensionnés
            pygame.transform.smoothscale(barrel, (int(dimensions_list[0][0]), int(dimensions_list[0][1]))).convert_alpha(),
            pygame.transform.smoothscale(car, (int(dimensions_list[1][0]), int(dimensions_list[1][1]))).convert_alpha()
        ]

        self.obstacles_height: int = screen_height - 250 # Hauteur à laquelle les obstacles seront générés
        self.able_to_generate: bool = True # Permet de savoir si on peut générer un obstacle (pour éviter d'en générer plusieurs en même temps)

    def generate_obstacle(self, screen: pygame.Surface) -> None:
        """
        Génère un obstacle à une position aléatoire sur l'axe des x
        screen: surface sur laquelle l'obstacle sera affiché
        """
        obstacle = Obstacle(self.obstacles[randint(0, len(self.obstacles) - 1)], screen.get_width() + 50, self.obstacles_height)
        self.obstacles_group.add(obstacle)

    def update(self, screen: pygame.Surface, player_speed: int) -> None:
        """
        Met à jour la position des obstacles
        player_speed: vitesse du joueur
        screen: surface sur laquelle les obstacles seront affichés
        """
        self.obstacles_group.update(player_speed)
        self.obstacles_group.draw(screen)

        if self.able_to_generate:
            if randint(0, 100) == 0:
                self.able_to_generate = False
                self.generate_obstacle(screen)
        else:
            if len(self.obstacles_group.sprites()) == 0:
                self.able_to_generate = True
    
    def is_ground_available(self, screen_width: int) -> bool:
        """
        Permet de savoir si le sol est disponible pour générer autre chose au sol
        """
        is_available: bool = True
        for obstacle in self.obstacles_group.sprites():
            if obstacle.rect.x > screen_width - obstacle.width - 100:
                is_available = False
        return is_available