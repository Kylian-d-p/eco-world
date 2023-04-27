import pygame


class BackgroundLayer(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, speed: int, pos: int) -> None:
        """
        Constructeur de la classe BackgroundLayer
        surface: surface de l'image
        speed: vitesse de déplacement
        pos: position x
        """
        super().__init__() # Appel du constructeur de la classe Sprite
        self.origin_image: pygame.Surface = surface # Image du layer
        self.width: int = surface.get_width() # Largeur du layer
        self.height: int = surface.get_height() # Hauteur du layer
        self.image = self.origin_image # Image du layer
        self.rect = self.image.get_rect() # Rectangle du layer
        self.rect.x: int = pos # Position x du layer
        self.rect.y: int = 0 # Position y du layer 
        self.speed: int = speed # Vitesse de déplacement

    def update(self, player_speed: int) -> None:
        """
        Met à jour la position du layer
        player_speed: vitesse du joueur
        """
        self.rect.x -= (self.speed * player_speed) # Déplacement du layer
        if self.rect.x <= -self.width: # Si le layer sort de l'écran
            self.rect.x += self.width * 2 # On le replace à la fin de l'écran
