import pygame


class BackgroundLayer(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, speed: int, pos: int) -> None:
        super().__init__()
        self.origin_image: pygame.Surface = surface
        self.width: int = surface.get_width()
        self.height: int = surface.get_height()
        self.image = self.origin_image
        self.rect = self.image.get_rect()
        self.rect.x: int = pos
        self.rect.y: int = 0
        self.speed: int = speed

    def update(self, player_speed: int) -> None:
        self.rect.x -= (self.speed * player_speed)
        if self.rect.x <= -self.width:
            self.rect.x += self.width * 2
