import pygame


class Player(pygame.sprite.Sprite):
    """
    Classe Player
    """

    def __init__(self) -> None:
        super().__init__()
        self.x: int = 0
        self.y: int = 670
        self.width: int = 120
        self.height: int = 180
        self.images: list[pygame.Surface] = [  # Liste des images du joueur
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_1.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_2.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_3.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_4.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_5.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_6.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_7.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_8.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_9.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_10.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_11.png").convert_alpha(), (self.width, self.height)),
            pygame.transform.smoothscale(pygame.image.load("assets/player/Olivier_walking_12.png").convert_alpha(), (self.width, self.height)),
        ]
        # Index de l'image dans la liste self.images correspondant à l'image active
        self.current_image: int = 0
        # Attribut qui permet de ralentir la mise à jour de l'image du personnage en comptant le nombre de mise à jour
        # et en ne changeant l'image que lorsque ce compteur vaut 2 puis ensuite le réinitialiser à 0
        self.update_count: int = 0
        # Booléen qui indique si il faut retourner l'image pour faire avancer le personnage vers la gauche
        self.do_flip: bool = False
        # Entier qui défini la vitesse du joueur
        self.speed: int = 15
        # Booléen qui indique si le joueur est en train de sauter
        self.jumping = False
        # Entier qui défini la hauteur max du saut
        self.jump_height = 200
        # Entier qui défini la vitesse du saut
        self.jump_speed = 15
        # Entier qui défini la hauteur actuelle du saut
        self.current_jump_height = 0
        # Entier qui défini si le joueur est en train de monter ou de descendre pendant son saut
        self.jump_direction = 0


    def update(self, screen_width: int, direction: int=-1) -> None:
        """
            Mets à jour l'image du personnage
            direction : entier naturel (-1 : repos; 0: gauche, 1: droite)
        """
        self.update_count += 1
        if self.update_count == 2:
            self.update_count = 0
            if direction != -1: # Si le joueur se dirige quelque part
                if self.current_image != len(self.images) - 1:
                    self.current_image += 1
                else:
                    self.current_image = 0
        self.move(direction, screen_width)
        if direction == 0:
            self.do_flip = True
        elif direction != -1:
            self.do_flip = False
        if self.jumping:
            self.jump_step()

    def jump(self):
        if not self.jumping:
            self.jumping = True

    def jump_step(self):
        if self.jumping:
            if self.jump_direction == 0:
                if self.current_jump_height < self.jump_height:
                    self.y -= self.jump_speed
                    self.current_jump_height += self.jump_speed
                else:
                    self.jump_direction = 1
            elif self.jump_direction == 1:
                if self.current_jump_height > 0:
                    self.y += self.jump_speed
                    self.current_jump_height -= self.jump_speed
                else:
                    self.jumping = False
                    self.jump_direction = 0

    def move(self, direction: int, screen_width: int) -> None:
        """
        Déplace le joueur dans une certaine direction (0: gauche, 1: droite)
        """
        if direction == 1:
            if self.x + self.width + self.speed < screen_width:
                self.x += self.speed
        elif direction == 0:
            if self.x > 0:
                self.x -= self.speed

    def draw(self, screen: pygame.Surface) -> None:
        if self.do_flip :
            screen.blit(pygame.transform.flip(self.images[self.current_image], True, False), (self.x, self.y))
        else:
            screen.blit(self.images[self.current_image], (self.x, self.y))
