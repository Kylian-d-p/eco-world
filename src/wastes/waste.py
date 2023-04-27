import pygame
from random import randint

class Waste(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, x, y, is_flying: bool=False, flying_speed: int=0) -> None:
        """
        Constructeur de la classe Waste
        surface: surface du déchet
        x: position x du déchet
        y: position y du déchet
        is_flying: si le déchet est un déchet volant
        flying_speed: vitesse du déchet volant
        """
        super().__init__() # Appel du constructeur de la classe Sprite
        self.origin_image: pygame.Surface = pygame.transform.smoothscale(surface, (surface.get_width() * 2, surface.get_height() * 2)).convert_alpha() # Redimensionne l'image
        self.image: pygame.Surface = self.origin_image # Image du déchet
        self.width: int = surface.get_width() # Largeur du déchet
        self.height: int = surface.get_height() # Hauteur du déchet
        self.rect = self.image.get_rect() # Rectangle du déchet
        self.rect.x: int = x # Position x du déchet
        self.rect.y: int = y # Position y du déchet
        self.flying_speed: int = flying_speed # Vitesse du déchet volant
        self.is_flying: bool = is_flying # Si le déchet est un déchet volant
        self.spinning_value: int = 0 # Valeur de rotation du déchet

    def update(self, player_speed: int, outside_screen_callback) -> None:
        """
        Met à jour la position du déchet
        player_speed: vitesse du joueur
        """
        self.rect.x -= player_speed + self.flying_speed # Déplacement du déchet
        if self.is_flying: # Si le déchet est un déchet volant
            self.spinning_value += randint(0, 5) * 2 # On fait tourner le déchet
            if self.spinning_value >= 360: # Si le déchet a fait un tour complet
                self.spinning_value = 0 # On remet la valeur de rotation à 0
            self.image = pygame.transform.rotate(self.origin_image, self.spinning_value).convert_alpha() # On fait tourner l'image
            self.rect = self.image.get_rect(center=self.rect.center) # On met à jour le rectangle du déchet
        
        if self.rect.x < -self.width - 100: # Si le déchet sort de l'écran
            self.kill() # On le supprime
            outside_screen_callback() # On appelle la fonction de callback

