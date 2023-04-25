import pygame


class Waste(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, speed: int, x, y) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.transform.smoothscale(
            surface, (surface.get_width() * 2, surface.get_height() * 2)).convert_alpha()
        self.width: int = surface.get_width()
        self.height: int = surface.get_height()
        self.rect = self.image.get_rect()
        self.rect.x: int = x
        self.rect.y: int = y

    def get_width(self) -> int:
        return self.width

    def update(self, player_speed: int) -> None:
        """
        Met à jour la position du déchet
        """
        self.rect.x -= player_speed
