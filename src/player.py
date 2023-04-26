import pygame


class Player(pygame.sprite.Sprite):
    """
    Classe Player
    """

    def __init__(self, screen_height) -> None:
        super().__init__()
        self.width: int = 120
        self.height: int = 180
        self.images: list[pygame.Surface] = [  # Liste des images du joueur
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_1.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_2.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_3.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_4.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_5.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_6.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_7.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_8.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_9.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_10.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_11.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_12.png").convert_alpha(), (self.width, self.height)),
        ]
        # On vérifie que toutes les images ont la même taille
        for image in self.images:
            assert image.get_width() == self.width and image.get_height() == self.height
        # Image active du joueur
        self.image: pygame.Surface = self.images[0]
        # Rectangle de l'image du joueur
        self.rect: pygame.Rect = self.image.get_rect()
        # Position de l'image du joueur
        self.rect.x: int = 0
        self.rect.y: int = screen_height - self.height
        # Index de l'image dans la liste self.images correspondant à l'image active
        self.current_image: int = 0
        # Attribut qui permet de ralentir la mise à jour de l'image du personnage en comptant le nombre de mise à jour
        # et en ne changeant l'image que lorsque ce compteur vaut 2 puis ensuite le réinitialiser à 0
        self.update_count: int = 0
        # Booléen qui indique si le joueur est en train de sauter
        self.jumping = False
        # Vecteur qui défini la vélocité du joueur
        self.velocity = pygame.math.Vector2()
        # Entier qui défini la vélocité en y du joueur
        self.velocity.y = 0
        # Entier qui défini la vélocité en x du joueur
        self.velocity.x = 0
        # Entier qui défini la vélocité maximale en x du joueur
        self.max_x_velocity = 50
        # Entier qui défini la force du déplacement du joueur lorsqu'il appuie sur une touche
        self.moving_speed_x = 5
        # Entier qui défini la vitesse de décélération du joueur lorsqu'il ne bouge pas
        self.stopping_speed_x = 2

    def update(self, screen_width: int, screen_height: int, direction: int = -1) -> None:
        """
            Mets à jour l'image du personnage
            direction : entier naturel (-1 : repos; 0: gauche, 1: droite)
        """
        self.update_count += 1
        if self.update_count == 2:
            self.update_count = 0
            if self.current_image != len(self.images) - 1:
                self.current_image += 1
            else:
                self.current_image = 0

        if -self.max_x_velocity + self.moving_speed_x < self.velocity.x < self.max_x_velocity - self.moving_speed_x:
            if direction == 0:
                self.velocity.x -= self.moving_speed_x
            elif direction == 1:
                self.velocity.x += self.moving_speed_x
        
        if self.velocity.x > 0 and self.rect.x + self.width + self.velocity.x < screen_width:
            self.rect.x += self.velocity.x
        elif self.velocity.x < 0 and self.rect.x > 0:
            self.rect.x += self.velocity.x
        else:
            self.velocity.x = 0        

        if self.velocity.x > 0:
            self.velocity.x -= self.stopping_speed_x
        elif self.velocity.x < 0:
            self.velocity.x += self.stopping_speed_x

        if self.jumping:
            self.rect.y -= self.velocity.y
            self.velocity.y -= 2
            if screen_height - self.height <= self.rect.y:
                self.jumping = False
                self.rect.y = screen_height - self.height
                self.velocity.y = 0


    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.velocity.y = 40

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.images[self.current_image], (self.rect.x, self.rect.y))
