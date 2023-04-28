import pygame


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, pos_x: int, pos_y: int) -> None:
        """
        Constructeur de la classe Obstacle
        surface: surface de l'image
        pos_x: position x
        pos_y: position y
        """
        super().__init__() # Appel du constructeur de la classe Sprite
        self.origin_image: pygame.Surface = surface # Image de l'obstacle
        self.width: int = surface.get_width() # Largeur de l'obstacle
        self.height: int = surface.get_height() # Hauteur de l'obstacle
        self.image = self.origin_image # Image de l'obstacle
        self.rect = self.image.get_rect() # Rectangle de l'obstacle
        self.rect.x: int = pos_x # Position x de l'obstacle
        self.rect.y: int = pos_y # Position y de l'obstacle

    def update(self, player_speed: int) -> None:
        """
        Met à jour la position de l'obstacle
        player_speed: vitesse du joueur
        """
        self.rect.x -= player_speed # Déplacement de l'obstacle
        if self.rect.x <= -self.width: # Si l'obstacle sort de l'écran
            self.kill() # On le supprime