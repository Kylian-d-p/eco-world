import pygame


class Player(pygame.sprite.Sprite):
    """
    Classe Player
    """

    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 600
        self.images: list[pygame.Surface] = [  # Liste des images du joueur
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_1.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_2.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_3.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_4.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_5.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_6.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_7.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_8.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_9.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_10.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_11.png").convert_alpha(), (120, 180)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_12.png").convert_alpha(), (120, 180)),
        ]
        # Index de l'image dans la liste self.images correspondant à l'image active
        self.current_image: int = 0
        # Attribut qui permet de ralentir la mise à jour de l'image du personnage en comptant le nombre de mise à jour
        # et en ne changeant l'image que lorsque ce compteur vaut 3 puis ensuite le réinitialiser à 0
        self.update_count: int = 0

    def update(self) -> None:
        if self.current_image != len(self.images) - 1:
            self.current_image += 1
        else:
            self.current_image = 0

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.images[self.current_image], (self.x, self.y))
