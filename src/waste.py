import pygame
from random import randint

class Waste(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, x, y, is_flying: bool=False, flying_speed: int=0) -> None:
        super().__init__()
        self.origin_image: pygame.Surface = pygame.transform.smoothscale(surface, (surface.get_width() * 2, surface.get_height() * 2)).convert_alpha()
        self.image: pygame.Surface = self.origin_image
        self.width: int = surface.get_width()
        self.height: int = surface.get_height()
        self.rect = self.image.get_rect()
        self.rect.x: int = x
        self.rect.y: int = y
        self.flying_speed: int = flying_speed
        self.is_flying: bool = is_flying
        self.spinning_value: int = 0

    def update(self, player_speed: int) -> None:
        """
        Met à jour la position du déchet
        """
        self.rect.x -= player_speed + self.flying_speed
        if self.is_flying:
            self.spinning_value += randint(0, 5) * 2
            if self.spinning_value >= 360:
                self.spinning_value = 0
            self.image = pygame.transform.rotate(self.origin_image, self.spinning_value).convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)
        
        if self.rect.x < -self.width - 100:
            self.kill()

    def collided(self, sprite: pygame.sprite.Sprite) -> None:
        """
        Supprime tous les déchets sauf le sprite passé en paramètre
        """
        if sprite != self:
            self.kill()

