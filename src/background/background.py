import pygame
from background.layer import BackgroundLayer
from background.third_layer import ThirdLayer


class Background():
    """
    Classe Background permettant de gérer la parallaxe entre les différents layers du fond ainsi que l'animation des éloliennes
    """

    def __init__(self, screen_width: int, screen_height: int) -> None:
        """
        Constructeur du background prenant en argument la surface screen
        """
        self.third_layer: list[pygame.Surface] = [  # Liste des images du 3ème layer du background
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_1.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_2.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_3.PNG").convert_alpha(),  (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_4.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_5.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_6.PNG").convert_alpha(),  (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_7.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_8.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_9.PNG").convert_alpha(),  (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_10.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_11.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_3_12.PNG").convert_alpha(),  (screen_width, screen_height)).convert_alpha(),
        ]
        self.layer_images: list[pygame.Surface] = [  # Liste de tous les layers
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_7.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_6.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_5.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_4.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            # On va commencer l'animation au premier layer
            self.third_layer[0],
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_2.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/montagne/montagne_1.PNG").convert_alpha(), (screen_width, screen_height)).convert_alpha()
        ]

        # Liste de toutes les vitesses de chaque layer
        layer_speeds: list[float] = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        # Groupe de tous les layers
        self.layerGroup: pygame.sprite.Group = pygame.sprite.Group()
        # On ajoute tous les layers au groupe en utilisant la classe Layer
        for i in range(len(self.layer_images)):
            for j in range(0, 2):
                if i == 4:  # Si c'est le troisième layer
                    # On ajoute toutes les images du troisième layer
                    layer = ThirdLayer(
                        self.third_layer, layer_speeds[i], j * screen_width)
                    self.layerGroup.add(layer)
                else:
                    layer = BackgroundLayer(
                        self.layer_images[i], layer_speeds[i], j * screen_width)
                    self.layerGroup.add(layer)

    def update(self, screen: pygame.Surface, player_speed: int) -> None:
        """
        Afficher les layers sur screen
        """
        self.layerGroup.update(player_speed) # On met à jour les layers
        self.layerGroup.draw(screen) # On les affiche
