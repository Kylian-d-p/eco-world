import pygame


class Background(pygame.sprite.Sprite):
    """
    Classe Background permettant de gérer la parallaxe entre les différents layers du fond ainsi que l'animation des éloliennes
    """

    def __init__(self, screen: pygame.Surface) -> None:
        """
        Constructeur du background prenant en argument la surface screen
        """
        super().__init__()
        self.third_layer: list[pygame.Surface] = [  # Liste des images du 3ème layer du background
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_1.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_2.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_3.PNG").convert_alpha(),  (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_4.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_5.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_6.PNG").convert_alpha(),  (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_7.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_8.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_9.PNG").convert_alpha(),  (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_10.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_11.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_3_12.PNG").convert_alpha(),  (screen.get_width(), screen.get_height())),
        ]
        # Entier compris entre 0 et 2 indiquant quel est l'image active pour le troisième layer
        self.third_layer_int: int = 1
        self.layer_images: list[pygame.Surface] = [  # Liste de tous les layers
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_7.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_6.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_5.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_4.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            # On va commencer l'animation au premier layer
            self.third_layer[0],
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_2.PNG").convert_alpha(), (screen.get_width(), screen.get_height())),
            pygame.transform.scale(pygame.image.load("assets/montagne/montagne_1.PNG").convert_alpha(), (screen.get_width(), screen.get_height()))
        ]
        # Liste de toutes les vitesses de chaque layer
        self.layer_speeds: list[int] = [x for x in range(1, 8)]
        # Liste de toutes les positions de chaque layer
        self.layer_positions: list[int] = [0] * len(self.layer_images)

    def update(self) -> None:
        """
        Mise à jour de la position des layers
        """
        for i in range(len(self.layer_images)):
            self.layer_positions[i] -= self.layer_speeds[i]
            if self.layer_positions[i] < -self.layer_images[i].get_width():
                self.layer_positions[i] = 0

    def draw(self, screen: pygame.Surface) -> None:
        """
        Afficher les layers sur screen
        """
        for i in range(len(self.layer_images)):  # Pour chaque layer
            # On l'affiche
            screen.blit(self.layer_images[i], (self.layer_positions[i], 0))
            # On en affiche un autre à côté pour que l'écran soit rempli
            screen.blit(
                self.layer_images[i], (self.layer_positions[i] + self.layer_images[i].get_width(), 0))

        # Mise à jour de l'image du 3ème layer
        # Si l'image du troisième layer n'est pas la dernière de la liste
        if self.third_layer_int != len(self.third_layer) - 1:
            self.third_layer_int += 1  # On incrémente le compteur
            # On change l'image du 3ème layer pour passer à la suivante
            self.layer_images[4] = self.third_layer[self.third_layer_int]
        else:
            self.third_layer_int = 0  # On remet le compteur à 0
            # On change l'image du 3ème layer pour passer à la première
            self.layer_images[4] = self.third_layer[0]
