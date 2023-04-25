import pygame


class Waste(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, speed: int, x, y) -> None:
        super().__init__()
        self.origin_image: pygame.Surface = pygame.transform.smoothscale(surface, (surface.get_width() * 2, surface.get_height() * 2)).convert_alpha()
        self.width: int = surface.get_width()
        self.height: int = surface.get_height()
        self.speed: int = speed
        self.spinning_speed: int = 25
        self.spinning_value: int = 0
        self.image = pygame.transform.rotate(self.origin_image, self.spinning_value).convert_alpha()
        self.rect = self.origin_image.get_rect()
        self.rect.x: int = x
        self.rect.y: int = y

    def get_width(self) -> int:
        return self.width
    
    def update(self) -> None:
        """
        Met à jour la position du déchet
        """

        self.rect.x -= self.speed
        self.spinning_value += self.spinning_speed
        if self.spinning_value >= 360:
            self.spinning_value = 0
        self.image = pygame.transform.rotate(self.origin_image, self.spinning_value).convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)
        



