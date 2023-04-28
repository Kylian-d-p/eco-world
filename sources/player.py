import pygame


class Player(pygame.sprite.Sprite):
    """
    Classe Player
    """

    def __init__(self, screen_height) -> None:
        """
            Constructeur du joueur
            screen_height: Hauteur de l'écran
        """
        super().__init__() # Appel du constructeur de la classe Sprite
        self.width: int = 120 # Dimensions du joueur
        self.height: int = 180 # Dimensions du joueur
        self.images: list[pygame.Surface] = [  # Liste des images du joueur
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_1.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_2.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_3.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_4.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_5.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_6.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_7.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_8.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_9.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_10.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_11.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
            pygame.transform.smoothscale(pygame.image.load(
                "assets/player/Olivier_walking_12.png").convert_alpha(), (self.width, self.height)).convert_alpha(),
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
        # Booléen qui indique si le joueur a utilisé son double saut
        self.double_jump_used = False

    def update(self, screen_width: int, screen_height: int, direction: int = -1) -> None:
        """
            Mets à jour l'image du personnage et sa position
            screen_width : largeur de l'écran
            screen_height : hauteur de l'écran
            direction : entier naturel (-1 : repos; 0: gauche, 1: droite)
        """
        # On incrémente le compteur de mise à jour de l'image
        self.update_count += 1
        # On change l'image du personnage si le compteur de mise à jour de l'image vaut 2
        if self.update_count == 2:
            # On réinitialise le compteur de mise à jour de l'image
            self.update_count = 0
            # On change l'image du personnage
            if self.current_image != len(self.images) - 1:
                # Si l'image active n'est pas la dernière de la liste, on incrémente l'index de l'image active
                self.current_image += 1
            else:
                # Sinon, on réinitialise l'index de l'image active
                self.current_image = 0
        
        if -self.max_x_velocity + self.moving_speed_x < self.velocity.x < self.max_x_velocity - self.moving_speed_x: # Si la vélocité en x est inférieure à la vélocité maximale en x
            if direction == 0: # Si le joueur va à gauche
                self.velocity.x -= self.moving_speed_x # On augmente la vélocité en x vers la gauche
            elif direction == 1: # Si le joueur va à droite
                self.velocity.x += self.moving_speed_x # On augmente la vélocité en x vers la droite
        
        if self.velocity.x > 0 and self.rect.x + self.width + self.velocity.x < screen_width: # Si la vélocité en x est positive et que le joueur ne dépasse pas l'écran à droite
            self.rect.x += self.velocity.x # On déplace le joueur vers la droite
        elif self.velocity.x < 0 and self.rect.x > 0: # Si la vélocité en x est négative et que le joueur ne dépasse pas l'écran à gauche
            self.rect.x += self.velocity.x # On déplace le joueur vers la gauche
        else: # Si le joueur dépasse l'écran
            self.velocity.x = 0 # On réinitialise la vélocité en x à 0

        if self.velocity.x > 0: # Si la vélocité en x est positive
            self.velocity.x -= self.stopping_speed_x # On diminue la vélocité en x
        elif self.velocity.x < 0: # Si la vélocité en x est négative
            self.velocity.x += self.stopping_speed_x # On augmente la vélocité en x

        if self.jumping: # Si le joueur est en train de sauter
            if self.rect.y < 0: # Si le joueur dépasse l'écran en haut
                self.rect.y = 0 # On réinitialise la position en y à 0
                self.velocity.y = 0 # On réinitialise la vélocité en y à 0
            self.rect.y -= self.velocity.y # On déplace le joueur vers le haut
            self.velocity.y -= 2 # On diminue la vélocité en y
            if screen_height - self.height <= self.rect.y: # Si le joueur touche le sol
                self.jumping = False # On indique que le joueur n'est plus en train de sauter
                self.double_jump_used = False  # On indique que le joueur peut à nouveau utiliser son double saut
                self.rect.y = screen_height - self.height # On réinitialise la position en y à la position maximale en y
                self.velocity.y = 0 # On réinitialise la vélocité en y à 0

    def jump(self):
        """
            Fait sauter le joueur
        """
        if not self.jumping: # Si le joueur n'est pas en train de sauter
            self.jumping = True # On indique que le joueur est en train de sauter
            self.velocity.y = 40 # On augmente la vélocité en y
        elif not self.double_jump_used and self.velocity.y <= 25: # Si le joueur n'a pas utilisé son double saut et que sa vélocité en y est inférieure à 25
            self.velocity.y = 40 # On augmente la vélocité en y
            self.double_jump_used = True # On indique que le joueur a utilisé son double saut


    def draw(self, screen: pygame.Surface) -> None:
        """
            Dessine le personnage sur l'écran
            screen : surface sur laquelle dessiner le personnage
        """
        screen.blit(self.images[self.current_image], (self.rect.x, self.rect.y)) # On dessine l'image active du personnage sur l'écran
